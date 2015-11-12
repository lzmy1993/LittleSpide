# -*- coding: UTF-8 -*-
import urllib
import uuid
endWithArr = ['.pdf','.html','.doc','.docx','.png','.jpg','.gif','.txt','.xml','.ppt','.xls','.xlsx']

def cbk(a, b, c):
    '''回调函数
    @a: 已经下载的数据块
    @b: 数据块的大小
    @c: 远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print '%.2f%%' % per
def downloadHtml(url):
    fileName = uuid.uuid1().get_hex()
    for str in endWithArr:
        if url.endswith(str):
            fileName = fileName + str
            break
    else:
        fileName = fileName + '.html'
    local = '在这里输入你想要保存下载文件的路径/%s' % (fileName)
    urllib.urlretrieve(url, local, cbk)