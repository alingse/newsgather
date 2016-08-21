#coding=utf-8
#author@alingse
#2016.08.21

from importlib import import_module
import sys
import os

def load_sites(home='sites'):
    slist = []

    path = os.path.join(os.path.dirname(__file__),home)

    files = os.listdir(path)
    files.remove('__init__.py')

    for file in files:
        if file.startswith('_') and file.endswith('.py'):
            name = file.strip('.py')
            try:
                m = import_module('{}.{}'.format(home,name))
                s = getattr(m,name.strip('_'))
                slist.append(s)
            except Exception as e:
                print(e)
                pass

    return slist

if __name__ == '__main__':
    slist = load_sites()
    print(slist)
    #_cnblogs = __import__('sites._cnblogs')
    #print(_cnblogs.cnblogs.seeds)