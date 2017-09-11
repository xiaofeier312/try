from gevent import monkemy
import gevent
import urllib2, time

url = 'http://ebooking.elong.com'


def f(url):
    resp = urllib2.urlopen(url)
    data = resp.read()
    print('data is :', data)


gevent.joinall(
    [gevent.spawn(f, url)]
)


def myprint():
    start = time.time()
    for x in range(1, 1001):
        print ('hello, world')
    end = time.time()
    print ('endtime:', (end - start))
# from asynchttp import Http
#
#
# http = Http()
# url = 'http://ebooking.elong.com'
# respone, content = http.request(url)
#


# import matplotlib.pyplot as plt
# import numpy as np
#
#
# list1 =[x for x in range(10) ]
# list2 = [111,112,113,121,122,123,124,125,126,127]
# list3 = [1,3,5,7,7,8,8,88,8,8]
# plt.plot(list1,list2,label='$haha1$',color='red',linewidth=2)
# plt.plot(list1,list3,"b--",label='$hehe2')
# plt.xlabel('time')
# plt.ylabel('money')
# plt.title('test he')
# plt.ylim(-1.2,150.2)
#





if __name__ == '__main__':
    #print respone
    print ('oever')
    myprint()
