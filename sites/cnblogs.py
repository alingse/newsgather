#coding=utf-8
#author@alingse
#2016.08.16


import requests
from pyquery import PyQuery as pq
from dateutil.parser import parse as timeparse

import json
import re

from utils import config
from utils import _site
from utils import _tails_set

cnblogs = _site()

cnblogs.host = 'www.cnblogs.com'

cnblogs.allow_hosts_matchs = [re.compile('^.*\.cnblogs\.com$').match]

def gen_seeds():
    seeds = []    
    seeds.append('http://www.cnblogs.com/AllBloggers.aspx')
    seeds.append('https://www.cnblogs.com/')
    seeds.append('http://www.cnblogs.com/expert/')
    seeds.append('http://www.cnblogs.com/pick/')
    seeds.append('http://www.cnblogs.com/candidate/')

    return seeds

cnblogs.seeds = gen_seeds()


_url_re = re.compile('^http://www\.cnblogs\.com/[^/]+/(p|articles)/[0-9]+\.html$')
_url_re2 = re.compile('^http://www\.cnblogs\.com/[^/]+/archive/\d{4}/\d{2}/\d{2}/\d+\.html$')

cnblogs.url_matchs = [_url_re.match,_url_re2.match]


_index_re = re.compile('^http://www\.cnblogs\.com/[^/]+/$')
_index_re2 = re.compile('^http://www\.cnblogs\.com/cate/\d+/$')
_index_re3 = re.compile('^http://www\.cnblogs\.com/[^/]+/category/\d+\.html$')
_index_re4 = re.compile('^http://www\.cnblogs\.com/.*/$')

cnblogs.index_matchs = [_index_re.match,_index_re2.match,_index_re3.match,_index_re4.match]

cnblogs.invalid_tails = _tails_set

def req_html(url,encode='utf-8',**kwargs):
    headers = {
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6", 
        "Accept-Encoding": "gzip, deflate, sdch", 
        "Host": "www.cnblogs.com", 
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
        "Upgrade-Insecure-Requests": "1", 
        "Connection": "keep-alive", 
        "Pragma": "no-cache", 
        "Cache-Control": "no-cache", 
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    }
    try:
        if 'headers' not in kwargs:
            kwargs['headers'] = headers
        if 'timeout' not in kwargs:
            kwargs['timeout'] = 3
        r = requests.get(url,**kwargs)
        html = r.content.decode(encode).strip()
        return html
    except Exception as e:
        pass


def req_meta(url,**kwargs):
    html = req_html(url,**kwargs)
    if html == None:
        return None
    try:
        htmld = pq(html)
        meta = {}
        meta['title'] = htmld('.postTitle2').text()
        meta['posttime'] = timeparse(htmld('#post-date').text())
        meta['content'] = htmld('#cnblogs_post_body').text()
        meta['nick'] = htmld('#Header1_HeaderTitle').text()

        parts = url[:-5].split('/')
        u = parts[3]
        postid = parts[-1]
        
        meta['username'] = u

        view = req_html('http://www.cnblogs.com/mvc/blog/ViewCountCommentCout.aspx?postId='+postid)
        meta['view'] = int(view) if view else 0
        comment = req_html('http://www.cnblogs.com/mvc/blog/GetComments.aspx?postId='+postid+\
                            '&blogApp='+u+\
                            '&pageIndex=0&anchorCommentId=0&_=1471419238926')

        #meta['comment'] = json.loads(comment)['commentCount'] if comment else 0
        meta['comment'] = int(comment[16:comment.find(',')]) if comment else 0

        return meta
    except Exception as e:
        print(e)

cnblogs.req_meta = req_meta


if __name__ == '__main__':
    url = 'http://www.cnblogs.com/dissun/articles/5745896.html'
    hit = False
    for match in cnblogs.url_matchs:
        if match(url):
            hit = True
            break
    if hit:
        meta = cnblogs.req_meta(url)
        print(meta)