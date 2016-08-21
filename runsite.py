#coding=utf-8
#author@aingse
#2016.08.21

from threading import Thread
from Queue import Empty,Queue

#从一端取再放入另一端
#或者是注册函数
class siteRun(Thread):

    def __init__(self):
        super(siteRun,self).__init__()
        pass

    def run(self):
        pass