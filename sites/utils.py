#coding=utf-8
#author@alingse
#2016.08.15


class config(object):

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError, "Can't reset the const{0}".format(name)
        self.__dict__[name] = value

    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        return None


class _site(config):
    def __init__(self):
        super(_site,self).__init__()
        #self.__setattr__('func',self.func)


_tails = ['.js','.css','.jpg','.jpeg','.png','.gif','.svg','.pdf','.icon','.mp3']
_tails_set = set(_tails+map(str.upper,_tails))
        
if __name__ == '__main__':
    pass
    #print(invalid_tails)