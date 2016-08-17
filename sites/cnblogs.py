#coding=utf-8
#author@alingse
#2016.08.16

from pyquery import PyQuery as pq
import requests
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

cnblogs.indexs = []

_url_re = re.compile('^http://www\.cnblogs\.com/[^/]+/(p|articles)/[0-9]+\.html$')
_url_re2 = re.compile('^http://www\.cnblogs\.com/[^/]+/archive/\d{4}/\d{2}/\d{2}/\d+\.html$')

cnblogs.url_matchs = [_url_re.match,_url_re2.match]


_index_re = re.compile('^http://www\.cnblogs\.com/[^/]+/$')
_index_re2 = re.compile('^http://www\.cnblogs\.com/cate/\d+/$')
_index_re3 = re.compile('^http://www\.cnblogs\.com/[^/]+/category/\d+\.html$')

cnblogs.index_matchs = [_index_re.match,_index_re2.match,_index_re3.match]

cnblogs.invalid_tails = _tails_set


if __name__ == '__main__':
    pass