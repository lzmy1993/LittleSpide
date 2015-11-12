# LittleSpide
a little web spide
这里主要介绍整个库的架构:<br>
>>使用语言：python2.7<br>
>>平台：Mac OS<br>
>>需要安装的第三方库：BeautifulSoup，BitVector<br>
>>文件:<br>
>>>>1.main.py 是程序的主函数文件<br>
>>>>>>下载所有文件后，安装缺少的库，之后运行该文件即可，如果想修改种子地址，请在main函数只能怪修改run()的参数，<br>
>>>>>>默认为'http://computer.hdu.edu.cn'，并且分析你要爬的网站URL的组成，在is_needURL()函数中，修改防止爬到外网地址的信息。<br>
>>>>2.download.py 是主要的下载函数文件<br>
>>>>>>下载文件类型：['.pdf','.html','.doc','.docx','.png','.jpg','.gif','.txt','.xml','.ppt','.xls','.xlsx']<br>
>>>>>>请在这里的下载函数内，修改变量local的值为你想保存下载文件的路径<br>
>>>>3.bloomFilter.py 是实现布隆过滤的文件(说明，该文件是其他开发者的开源文件，我只是做了点修改)<br>
>>>>>>bloomFilter里使用了BitVector库，请自行到网路上下载
