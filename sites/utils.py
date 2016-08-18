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


tails = ['.js','.css','.jpg','.jpeg','.png','.gif','.svg','.pdf','.icon','.mp3']
tails_set = set(_tails+map(str.upper,_tails))

user_agents = config()
if True:
    user_agents.mobile = []
    user_agents.mobile.append("Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5")
    user_agents.mobile.append("Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5")
    user_agents.mobile.append("Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5")
    user_agents.mobile.append("Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    user_agents.mobile.append("MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    user_agents.mobile.append("Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10")
    user_agents.mobile.append("Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13")
    user_agents.mobile.append("Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+")
    user_agents.mobile.append("Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0")
    user_agents.mobile.append("Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124")
    user_agents.mobile.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)")
    user_agents.mobile.append("UCWEB7.0.2.37/28/999")
    user_agents.mobile.append("NOKIA5700/ UCWEB7.0.2.37/28/999")
    user_agents.mobile.append("Openwave/ UCWEB7.0.2.37/28/999")
    user_agents.mobile.append("Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999")

if True:
    user_agents.pc = []
    user_agents.pc.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)")
    user_agents.pc.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)")
    user_agents.pc.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)")
    user_agents.pc.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)")
    user_agents.pc.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)")
    user_agents.pc.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)")
    user_agents.pc.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)")
    user_agents.pc.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)")
    user_agents.pc.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
    user_agents.pc.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11")
    user_agents.pc.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)")
    user_agents.pc.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)")
    user_agents.pc.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50")
    user_agents.pc.append("Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1")
    user_agents.pc.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50")
    user_agents.pc.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;")
    user_agents.pc.append("Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11")
    user_agents.pc.append("Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11")

if __name__ == '__main__':
    pass
    #print(invalid_tails)