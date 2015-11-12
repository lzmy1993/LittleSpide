# -*- coding: UTF-8 -*-
import urllib
from bs4 import BeautifulSoup
from bloomFilter import BloomFilter
import Queue
import socket
socket.setdefaulttimeout(6)
from download import downloadHtml

endWithArr = ['.pdf','.html','.doc','.docx','.png','.jpg','.gif','.txt','.xml','.ppt','.xls','.xlsx']           #资源文件

#根据popurl获取绝对路径
def get_absoluteUrlHead(url):
    index = url.find('//')
    urlLen = len(url)
    urlSub = url[index+2:urlLen]
    indexSub = urlSub.find('/')
    totalIndex = index + indexSub + 3
    absoluteUrlHead = url[0:totalIndex]
    return absoluteUrlHead

#判断相对/绝对路径(例如输入:http://www.baidu.com/index/ss输出:http://www.baidu.com/ )
def is_relativeURL(url,seed):
    if url == '#' or url == '/' or url.startswith('javascript'):
        return -1   #无用URL
    index = url.find('//')
    if index == -1:
        absoluteurl = get_absoluteUrlHead(seed) + url
        return absoluteurl  #拼接好的绝对路径
    return url      #绝对路径

#判断是否需要爬
def is_needURL(url):
    if 'hdu.edu.cn' in url:
        if url.startswith('mailto'):
            return False
        else:
            return True
    return False

#判断是否是资源文件
def is_resourceFile(url):
    for str in endWithArr:
        if url.endswith(str):
            return True
        else:
            continue
    return False

#转码
def to_bytestring(s,enc='utf-8'):
    if s:
        if isinstance(s, str):
            return s
        else:
            return s.encode(enc)

#用队列广度优先获取URL
def run(seed):
    bf = BloomFilter(0.00001,1000000)   #初始化布隆过滤器
    queue = Queue.Queue(maxsize = 0)        #初始化URL队列
    urlCount = 0                        #初始化已得到URL变量
    urlList = []                        #初始化下载列表
    queue.put(seed)
    
    while(queue.empty() == False):
        currentURL = queue.get()
        urlList.append(currentURL)
        print 'currentURL',to_bytestring(currentURL)
        
        try:    #timeout处理
            html = urllib.urlopen(currentURL)
        except:
            continue

        bs_obj = BeautifulSoup(html,'html.parser')
        a_list = bs_obj.findAll('a') + bs_obj.findAll('img')

        for aa in a_list:
            if aa.attrs.get('href'):
                hrefStr = aa.attrs.get('href')
            else:
                hrefStr = aa.attrs.get('src')

            if hrefStr:
                hrefStr = is_relativeURL(hrefStr,currentURL)
                if hrefStr == -1:     #判断相对/绝对路径
                    continue
                if is_needURL(hrefStr) == True:         #判断是否需要抓取
                    if bf.is_element_exist(hrefStr) == False:   #布隆过滤
                        bf.insert_element(hrefStr)
                        print to_bytestring(hrefStr)
                    if is_resourceFile(hrefStr) == False:  #判断是否是资源文件
                        queue.put(hrefStr)
                    
                    urlList.append(hrefStr)
                    try:
                        downloadHtml(hrefStr)
                    except:
                        pass
                    urlCount = urlCount + 1
        print '所有--当前',urlCount,len(urlList)

#主函数
if __name__ == "__main__":
    run('http://marxnew.hdu.edu.cn')

