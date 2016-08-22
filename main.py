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
#move to runsite?
from runutil import exit_all
from runutil import all_exited
from runutil import hold

import os


def execute(sitedb,sitereq,ctrl):
    link = sitedb.linkget()

    if link == None:
        empty = ctrl.get('empty',0)
        ctrl['empty'] = empty + 1
        return
    ctrl['empty'] = 0

    html = sitereq.req_html(link)
    if html == None:
        sitedb.linkput(link,check=False)
        return

    links = sitereq.html2links(link,html)
    urls,indexes = sitereq.shuffle(links)

    #put
    for index in indexes:
        sitedb.linkput(index)

    for url in urls:
        sitedb.linkput(url)

    #meta
    for url in urls:
        if sitedb.urlexists(url):
            continue
        if ctrl.get('exit'):
            return
        meta = sitereq.req_meta()
        if meta != None:
            sitedb.metasave(meta)
            sitedb.indexinc(link)
            sitedb.urlset(url)


def runsite(site,es,env,path):
    sitedb = siteDB(site,es,env,path)
    sitereq = siteReq(site)

    ctrl = {}
    args = (sitedb,sitereq,ctrl)

    #thct,diff
    runlist = init_runlist(execute,args=args,thct=5)

    diff = 0.5
    while sitedb.qsize() > 0 and ctrl.get('empty',0)>20:
        hold(diff)
    
    exit_all(runlist)
    while not all_exited(runlist):
        hold(diff)
    sitedb.save()
    sitedb.close()


def main():
    path = load_default_path()
    es = init_es()
    env = init_env(path)

    sitelist = load_sites()
    while True:
        for site in sitelist:
            runsite(site,es,env,path)
        hold(0.5*60*60)

if __name__ == '__main__':
    main()


