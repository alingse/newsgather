#coding=utf-8
#author@alingse
#2016.08.17

from __future__ import print_function

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
    def html2links(self,url,html):
        site = self.site
        host = site.host
        urld = urlparse.urlparse(url)
        #
        urlhost = '{0.scheme}://{0.netloc}'.format(urld)
        urlpath = urlhost + urld.path


        _hrefs = hreffind(html)
        links = []
        for href in _hrefs:
            if href.startswith('//'):
                href = href.strip('//')
            elif href.startswith('/'):
                href = urlhost + href
            elif '://' not in href:
                href = urlpath + href

            links.append(href)
        return links


    def shuffle(self,links):
        site = self.site
        urls = set()
        indexes = set()
        for link in links:
            linkd = urlparse.urlparse(link)

            #check - tail
            path = linkd.path
            tail = path[path.rfind('.'):]
            if tail in site.invalid_tails:
                continue

            '''
            #check - host
            host = linkd.netloc
            hit = False
            for match in site.allow_hosts_matches:
                if match(host):
                    hit = True
                    break
            if not hit:
                continue
            '''

            #urls
            hit = False
            for match in site.url_matches:
                if match(link):
                    hit = True
                    urls.add(link)
                    break
            if hit:
                continue

            #indexes
            for match in site.index_matches:
                if match(link):
                    indexes.add(link)
                    break

        urls = list(urls)
        indexes = list(indexes)
        return urls,indexes
        



if __name__ == '__main__':
    slist = load_sites()
    #from sites._cnblogs import cnblogs as site
    #from sites.sites import sitelist
    site = slist[0]

    url = choice(site.seeds)

    req = siteReq(site)
    html = req.req_html(url)
    #print(html)
    links = req.html2links(url,html)
    urls,indexes = req.shuffle(links)
    print('url')
    map(print,urls)
    print('index')
    map(print,indexes)