#coding=utf-8
#author@aingse
#2016.08.21

from threading import Thread
from Queue import Empty,Queue
from time import sleep
from operator import truth

#从一端取再放入另一端
#或者是注册函数
class runUnit(Thread):

    def __init__(self,execute,args=(),kwargs={},diff = 0.1):
        super(runUnit,self).__init__()
        self.execute = execute
        self.diff = diff
        self.args = args
        self.kwargs = kwargs
        self.exit = False
        self.exited = False
        

    def shutdown(self):
        self.exit = True

    def run(self):
        while not self.exit:
            self.execute(*self.args,**self.kwargs)
            hold(self.diff)
        #exit
        self.exited = True


def init_runlist(execute,args=(),kwargs={},diff=0.2,thct=5):
    runlist = []
    for i in range(thct):
        u = runUnit(execute,args=args,kwargs=kwargs,diff=diff)
        u.start()
        runlist.append(u)
    return runlist

def hold(diff=0.2):
    sleep(diff)

def exit_all(runlist):
    for unit in runlist:
        unit.shutdown()


def all_exited(runlist):
    runs = [u.isAlive() or not u.exited for u in runlist]
    runs = filter(truth,runs)
    return len(runs)


if __name__ == '__main__':
    def execute(c,a=4,b=2):
        print(a,b,c)
        sleep(0.3)
    args = [9]
    kwargs = dict(a=3,b=7)
    runlist = init_runlist(execute,args=args,kwargs=kwargs)
    sleep(5)
    exit_all(runlist)
    while all_exited(runlist) != True:
        print('check')
        sleep(0.1)


