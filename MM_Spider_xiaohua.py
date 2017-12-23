#coding=utf-8
import urllib
import re
for i in range(44):
    def getHtml(url):#获取网页内容
        page = urllib.urlopen(url)
        html = page.read()
        return html
        print html

    def getImg(html):#获取图片并且保存
        reg = r'src="(.+?\.jpg)"'
        imgre = re.compile(reg)
        imglist = re.findall(imgre,html)

        for j in range(len(imglist)):#比较恶心，有时候是绝对路径，有时候是相对路径，做个兼容

            if "http" in imglist[j]:
                imglist[j] = imglist[j]
            else:
               imglist[j]='http://www.xiaohuar.com'+imglist[j]

        print imglist
        d=0
        x=0
        for imgurl in imglist:
            urllib.urlretrieve(imgurl,'/Users/likun/PycharmProjects/MKMM/MKMM/MM_pic/%d.jpg' % x)
            d=d+1
            x=i*100+d


    m = str(i)
    url = "http://www.xiaohuar.com/list-1-"+m+".html"
    print url

    html = getHtml(url)
    print getImg(html)
