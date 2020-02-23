import os
def turn(f):
    f=f.replace('&amp;','&')
    f=f.replace('&apos;',"'")
    f=f.replace('&quot;','"')
    f=f.replace('&lt;','<')
    f=f.replace('&gt;','>')
    return f
Cindy='is fucked by Peter'
print(Cindy[-3:])
last=input("请输入要转移的文件后缀（*表示都要）")
for i in os.listdir(os.getcwd()):
    if i!='change.py' and (i[-3:]==last or i[-1]==last):
        fp=open(i,'r',encoding='utf-8')
        data=fp.read()
        data=turn(data)
        fp.close()
        fp=open(i,'w',encoding='utf-8')
        fp.write(data)
        fp.close()
        
