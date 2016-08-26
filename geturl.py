__author__ = 'lenovo'
import urllib
from bs4 import BeautifulSoup
import re

def get_all_url(url):
   urls = []
   web = urllib.urlopen(url)
   soup =BeautifulSoup(web.read(),"lxml")
   #print "4"
   tags_a =soup.findAll(name='a',attrs={'href':re.compile("^https?://")})
   #print "5"
   #print tags_a
   try :
        for tag_a in tags_a:
            urls.append(tag_a['href'])
            #print tag_a
   except:
        pass
   #print urls
   return  urls


def get_local_urls(url,sitename):
   local_urls = []
   urls = get_all_url(url)
   for _url in urls:
       ret = _url
       if sitename in ret.replace('//','').split('/')[0]:
           local_urls.append(_url)
   return  local_urls


def get_remote_urls(url,sitename):
   remote_urls = []
   #print "2"
   urls = get_all_url(url)
   #print "3"
   #print urls
   for _url in urls:
       ret = _url
       if sitename not in ret.replace('//','').split('/')[0]:
           remote_urls.append(_url)
   return  remote_urls

def __main__():
   #url = 'http://www.crifan.com/'
   sitename = 'mopon.cn'
   url = 'http://www.'+sitename

   #print url
   rurls = get_remote_urls(url,sitename)
   print "--------------------remote urls-----------------------"
   for ret in rurls:
       print ret
   print "---------------------localurls-----------------------"
   lurls = get_local_urls(url,sitename)
   for ret in lurls:
       print ret

if __name__ == '__main__':
 __main__()
