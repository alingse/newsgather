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

    def __init__(self,execute,diff = 0.1,**kwargs):
        super(runUnit,self).__init__()
        self.execute = execute
        self.diff = diff
        self.kwargs = kwargs
        self.exit = False
        self.exited = False
        

    def shutdown(self):
        self.exit = True

    def run(self):
        while not self.exit:
            self.execute(**self.kwargs)
            sleep(self.diff)
        #exit
        self.exited = True


def init_runlist(execute,diff=0.2,thct=5,**kwargs):
    runlist = []
    for i in range(thct):
        u = runUnit(execute,diff=diff,**kwargs)
        u.start()
        runlist.append(u)
    return runlist


def exit_all(runlist):
    for unit in runlist:
        unit.shutdown()


def all_exited(runlist):
    runs = filter(truth,[u.exited for u in runlist])
    if runs == []:
        return True
    return len(runs)


if __name__ == '__main__':
    def execute(a=4,b=2):
        print(a,b)
        sleep(0.3)

    runlist = init_runlist(execute,a=3,b=7)
    sleep(5)
    exit_all(runlist)
    while all_exited(runlist) != True:
        print('check')
        sleep(0.1)


