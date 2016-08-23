#coding=utf-8
#author@alingse
#2016.08.15

#from dbutils import init_env
from dbutils import load_url_visit_db
from dbutils import load_index_count_db
from dbutils import load_named_queue
from dbutils import truncate_named_queue

#from esutils import init_es
from esutils import bulk_post

import datetime

#统一几个不同作用的数据库
class siteDB(object):
    
    def __init__(self,site,es,env,datapath,essize=1000,maxsize=3000):
        self.site = site
        #es
        self.es = es
        self.essize = essize
        #db
        self.env = env
        self.datapath = datapath
        self.maxsize = maxsize

        name = self.site.host
        #truncate
        truncate_named_queue(env,name,datapath)
        queue = load_named_queue(env,name,datapath)

        url_visit = load_url_visit_db(env,name,datapath)
        index_count = load_index_count_db(env,name,datapath)

        #db
        self.name = name
        self.queue = queue
        self.url_visit = url_visit
        self.index_count = index_count
        self.set = set()
        
        #es
        self.metas = []

    def init(self):
        for seed in self.site.seeds:
            self.linkput(seed)

        for key,count in self.index_count.items():
            if int(count) > 0:
                self.linkput(key)

    def close(self):
        self.url_visit.close()
        self.index_count.close()
        self.queue.close()

    def qsize(self):
        return len(self.queue)

    def linkput(self,link,check=True):
        '''
        放入待请求队列
        '''
        if check:
            if link in self.set:
                return
        
        self.set.add(link)
        #unicode
        #256
        link = str(link)
        self.queue.append(link[:256])
        
        if len(self.set) >= self.maxsize:
            for i in range(self.maxsize/10):
                self.set.pop()

    def linkget(self):
        res = self.queue.consume()
        if res != None:
            link = res[1].strip()
            return link

    def urlexists(self,url):
        url = str(url)
        return self.url_visit.exists(url)

    def urlset(self,url):
        url = str(url)
        self.url_visit.put(url,'')

    def indexinc(self,index):
        index = str(index)
        cnt = self.index_count.get(index)
        if cnt == None:
            cnt = 0
        cnt = int(cnt) + 1
        self.index_count.put(index,str(cnt))

    def save(self,metas=None):
        #default save self
        if metas == None:
            metas = self.metas
            self.metas = []
        if metas == []:
            return
        bulk_post(self.es,docs=metas,id_field='url')


    def metasave(self,meta,quick=False):
        meta['savetime'] = datetime.datetime.now()
        meta['host'] = self.name

        if quick:
            self.save(metas=[meta])
            return
        self.metas.append(meta)
        if len(self.metas) >= self.essize:
            self.save()
        

if __name__ == '__main__':
    pass

