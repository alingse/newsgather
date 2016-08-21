#coding=utf-8
#author@alingse
#2016.08.17

from pyquery import PyQuery as pq
import urlparse
import re

from rqutils import load_sites

from random import choice
import json
import sys

hreffind = re.compile('href *= *[\'"]([^\'"<]*)').findall

class siteReq(object):

    def __init__(self, site):
        self.site = site

    def is_url(self,url):
        for match in self.site.url_matches:
            if match(url):
                return True

    def is_index(self,url):
        for match in self.site.index_matches:
            if match(url):
                return True

    @staticmethod
    def chg_ua(site,onlypc=None,onlymb=None):
        if onlymb and onlypc:
            #raise Exception("")
            return False
        #ua = site.headers['User-Agent']
        if onlypc:
            ualist = site.user_agents.pc
        elif onlymb:
            ualist = site.user_agents.mobile
        else:
            ualist = choice([site.user_agents.mobile,site.user_agents.pc])

        site.headers['User-Agent'] = choice(ualist)
        return True


    def chg_my_ua(self,**kwargs):

        return self.chg_ua(self.site,**kwargs)


    def req_html(self,url):
        self.chg_my_ua()
        html = self.site.req_html(url)
        return html


    def req_meta(self,url):
        self.chg_my_ua()
        meta = self.site.req_meta(url)
        return meta

    #the most important
    def html2hrefs(self,url,html):
        site = self.site
        host = site.host
        urlnow = urlparse.urlparse(url)

        hrefs = hreffind(html)
        for href in hrefs:
            hit = False
            if href.startswith('/'):
                if href.startswith('//'):
                    pass
                else:
                    pass
            
            for scheme in self.site.schemes:
                if href.startswith('{}://'.format(scheme)):
                    pass
            pass

        print(hrefs)



    @staticmethod
    def shuffle(urls):
        pass



if __name__ == '__main__':
    slist = load_sites()
    #from sites._cnblogs import cnblogs as site
    #from sites.sites import sitelist
    site = slist[0]

    url = choice(site.seeds)

    req = siteReq(site)
    html = req.req_html(url)
    #print(html)
    req.html2hrefs(url,html)
