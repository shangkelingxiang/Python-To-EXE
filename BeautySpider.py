import requests
import re,os
import shutil
headers={'Referer': 'https://www.mm131.net/xinggan/2717_2.html','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

class BeautySpider:
    def __init__(self,mode,code):
        self.mode=mode
        self.code=code
        self.page=1
        self.url="https://www.mm131.net/"+self.mode+"/"+self.code+".html"
        self.title=''
    def URL(self,page):
        if page==1:
            return self.url
        return "https://www.mm131.net/"+self.mode+"/"+self.code+"_"+str(self.page)+".html"
    def Index(self,name):
        if os.path.exists(name):
            shutil.rmtree(name)
        os.mkdir(name)
    def TurnToImage(self,x,content):
        fp=open(self.title+"/(图片"+str(x)+").jpg","wb")
        fp.write(content)
        fp.close()
    def GetTitle(self,text):
        return re.findall("<title>(.*?)_",text)[0]
    def GetImage(self,text):
        url=re.findall('<img alt=".*?" src="(.*?)"',text)[0]
        return requests.get(url,headers=headers).content
    def Loop(self):
        while True:
            r=self.URL(self.page)
            print(r)
            r=requests.get(r,headers=headers)
            if r.status_code==404:
                break
            r.encoding='gbk'
            self.TurnToImage(self.page,self.GetImage(r.text))
            self.page+=1
    def Work(self):
        r=requests.get(self.url,headers=headers)
        r.encoding='gbk'
        self.title=self.GetTitle(r.text)
        print(self.title)
        self.Index(self.title)
        self.Loop()
mode=input("请输入类型")
code=input("请输入编号")
Spider=BeautySpider(mode,code)
Spider.Work()
