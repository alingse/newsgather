#coding=utf-8
#author@alingse
#2016.08.15

import bsddb3
from bsddb3 import db
import os


dbpath = 'berkeley-db'
queuepath = 'queue'

url_visit_file = 'url.visit.db'
index_count_file = 'index.count.db'


def init_env(path):
    env = bsddb3.db.DBEnv()
    env.open(path,db.DB_CREATE|db.DB_INIT_CDB|db.DB_INIT_MPOOL)
    return env


def load_url_visit_db(env,path):
    uvdb = db.DB(env)
    uvfile = os.path.join(path,url_visit_file)
    uvdb.open(uvfile,db.DB_BTREE,db.DB_CREATE,0660)
    return uvdb


def load_index_count_db(env,path):
    icdb = db.DB(env)
    icfile = os.path.join(path,index_count_file)
    icdb.open(icfile,db.DB_BTREE,db.DB_CREATE,0660)
    return icdb


def named_queue_file(name,path):
    nqfile = os.path.join(path,queuepath,'{}.db'.format(name))
    return nqfile


def load_named_queue(name,env,path):
    nqueue = db.DB(env)
    nqueue.set_re_len(256)
    nqueue.set_re_pad(' ')
    nqfile = named_queue_file(name,path)
    nqueue.open(nqfile,db.DB_QUEUE,db.DB_CREATE,0660)

    return nqueue


def truncate_named_queue(name,env,path):
    nqueue = db.DB(env)
    nqueue.set_re_len(256)
    nqueue.set_re_pad(' ')
    nqfile = named_queue_file(name,path)
    nqueue.open(nqfile,db.DB_QUEUE,db.DB_CREATE,0660)
    
    fd = nqueue.fd()
    f = os.fdopen(fd,'w')
    f.truncate()
    f.close()


if __name__ == '__main__':
    
    pwd = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(pwd,'data',dbpath)    

    env = init_env(path)

    uvdb = load_url_visit_db(env,path)
    icdb = load_index_count_db(env,path)

    uvdb.close()
    icdb.close()
    
    nqueue = load_named_queue('test',env,path)
    nqueue.close()
    
    truncate_named_queue('test',env,path)
    
    env.close()



    