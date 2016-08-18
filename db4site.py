#coding=utf-8
#author@alingse
#2016.08.15

from dbutils import init_env
from dbutils import load_url_visit_db
from dbutils import load_index_count_db
from dbutils import load_named_queue
from dbutils import truncate_named_queue


#统一几个不同作用的数据库
class siteDB(object):
    
    def __init__(self,site,env,path,maxsize=2000):
        self.site = site
        
        name = self.site.host
        #truncate
        truncate_named_queue(name,env,path)
        queue = load_named_queue(name,env,path)

        url_visit = load_url_visit_db(env,path)
        index_count = load_index_count_db(env,path)

        self.env = env
        self.queue = queue
        self.url_visit = url_visit
        self.index_count = index_count
        self.set = set()
        self.maxsize = maxsize

    def init(self):
        for seed in self.site.seeds:
            self.put(seed)
        for key in self.index_count.keys():
            self.put(key)

    def put(self,href):
        '''
        放入待请求队列
        '''
        if href in self.set:
            return
        self.queue.append(href[:256])
        self.set.add(href)
        if len(self.set) >= self.maxsize:
            for i in range(maxsize/10):
                self.set.pop()

    def get(self):

        return self.queue.comsume()

    def exists(self,url):

        return self.url_visit.exists(url)

    def set(self,url):
        
        self.url_visit.put(url,'')

    def inc(self,index):
        cnt = self.index_count.get(index)
        if cnt == None:
            cnt = 0
        else:
            cnt = int(cnt) + 1
        self.index_count.put(index,str(cnt))

if __name__ == '__main__':
    pass

