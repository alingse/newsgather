#coding=utf-8
#author@alingse
#2016.08.16


import argparse

from db4site import siteDB
from reqsite import siteReq

from dbutils import load_default_path
from dbutils import init_env
from esutils import init_es

from requtil import load_sites
from runutil import init_runlist

import os


def execute(sitedb,sitereq):
    link = sitedb.linkget()
    if link == None:
        return
    html = sitereq.req_html(link)
    if html == None:
        sitedb.linkput(link,check=False)
        return
    links = sitereq.html2links(link,html)
    urls,indexes = sitereq.shuffle(links)

    #put
    for index in indexes:
        sitedb.linkput(index)

    #meta
    for url in urls:
        if sitedb.urlexists(url):
            continue
        sitedb.linkput(url)
        meta = sitereq.req_meta()
        if meta != None:
            sitedb.metasave(meta)
            sitedb.indexinc(link)
            sitedb.urlset(url)


def runsite(site,es,env,path):
    sitedb = siteDB(site,es,env,path)
    sitereq = siteReq(site)

    runlist = init_runlist(execute,sitedb,sitereq)
    







def main():
    
    path = load_default_path()
    es = init_es()
    env = init_env(path)

    sitelist = load_sites()


    












if __name__ == '__main__':
    main()


