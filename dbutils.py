#coding=utf-8
#author@alingse
#2016.08.15

import bsddb3
from bsddb3 import db
import os


dbpath = 'berkeley-db'
visitpath = 'visit'
indexpath = 'index'
queuepath = 'queue'

url_visit_file = '{}.url.visit.db'
index_count_file = '{}.index.count.db'
queue_file = '{}.queue.db'


def init_env(path):
    env = bsddb3.db.DBEnv()
    env.open(path,db.DB_CREATE|db.DB_INIT_CDB|db.DB_INIT_MPOOL)
    return env


def load_url_visit_db(env,name,path):
    uvdb = db.DB(env)
    uvfile = os.path.join(path,visitpath,url_visit_file.format(name))
    uvdb.open(uvfile,db.DB_BTREE,db.DB_CREATE,0660)
    return uvdb


def load_index_count_db(env,name,path):
    icdb = db.DB(env)
    icfile = os.path.join(path,indexpath,index_count_file.format(name))
    icdb.open(icfile,db.DB_BTREE,db.DB_CREATE,0660)
    return icdb


def load_named_queue(name,env,path):
    nqueue = db.DB(env)
    nqueue.set_re_len(256)
    nqueue.set_re_pad(' ')
    nqfile = os.path.join(path,queuepath,queue_file.format(name))
    nqueue.open(nqfile,db.DB_QUEUE,db.DB_CREATE,0660)

    return nqueue


def truncate_named_queue(name,env,path):
    nqueue = db.DB(env)
    nqueue.set_re_len(256)
    nqueue.set_re_pad(' ')
    nqfile = os.path.join(path,queuepath,queue_file.format(name))
    nqueue.open(nqfile,db.DB_QUEUE,db.DB_CREATE,0660)
    
    fd = nqueue.fd()
    f = os.fdopen(fd,'w')
    f.truncate()
    f.close()


if __name__ == '__main__':
    
    pwd = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(pwd,'data',dbpath)    

    env = init_env(path)

    name = 'test'
    uvdb = load_url_visit_db(env,name,path)
    icdb = load_index_count_db(env,name,path)
    uvdb.put('1','2')
    uvdb.get('1')
    uvdb.delete('1')
    uvdb.close()
    icdb.close()
    
    nqueue = load_named_queue('test',env,path)
    nqueue.append('1')
    print(len(nqueue))
    nqueue.close()
    truncate_named_queue('test',env,path)
    
    env.close()



    