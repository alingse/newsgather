#coding=utf-8
#author@alingse
#2016.08.17

from pyquery import PyQuery as pq
import requests

from random import choice

import json
import sys

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

    def __chg_ua(self):
        self.site.headers['User-Agent'] = choice(self.site.user_agents.pc)

    def req_html(self,url):
        self.__chg_ua()
        html = self.site.req_html(url)
        return html

    def req_meta(self,url):
        self.__chg_ua()
        meta = self.site.req_meta(url)
        return meta

    def parse_html(self,html):
        pass
        

if __name__ == '__main__':
    pass