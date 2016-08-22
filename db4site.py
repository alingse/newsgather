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


#统一几个不同作用的数据库
class siteDB(object):
    
    def __init__(self,site,es,env,datapath,essize=1000,maxsize=2000):
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
        truncate_named_queue(name,env,datapath)
        queue = load_named_queue(name,env,datapath)

        url_visit = load_url_visit_db(env,datapath)
        index_count = load_index_count_db(env,datapath)
        #db
        self.queue = queue
        self.url_visit = url_visit
        self.index_count = index_count
        self.set = set()
        
        #es
        self.metas = []

    def dbinit(self):
        for seed in self.site.seeds:
            self.put(seed)

        for key,count in self.index_count.items():
            if int(count) > 0:
                self.put(key)

    def close(self):
        self.url_visit.close()
        self.index_count.close()
        self.queue.close()


    def linkput(self,link,check=True):
        '''
        放入待请求队列
        '''
        if check:
            if link in self.set:
                return
        self.queue.append(link[:256])
        self.set.add(link)
        if len(self.set) >= self.maxsize:
            for i in range(maxsize/10):
                self.set.pop()

    def linkget(self):

        return self.queue.comsume()

    def urlexists(self,url):

        return self.url_visit.exists(url)

    def urlset(self,url):
        
        self.url_visit.put(url,'')

    def indexinc(self,index):
        cnt = self.index_count.get(index)
        if cnt == None:
            cnt = 0
        else:
            cnt = int(cnt) + 1
        self.index_count.put(index,str(cnt))

    def metasave(self,meta,quick=False):
        if quick:
            bulk_post(es,docs=[meta])    
        elif len(self.metas) < self.essize:
            self.metas.append(meta)
            return
        bulk_post(es,docs=self.metas)
        self.metas = []


if __name__ == '__main__':
    pass

