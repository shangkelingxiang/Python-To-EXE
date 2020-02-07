import os
def turn(f):
    f=f.replace('&amp;','&')
    f=f.replace('&apos;',"'")
    f=f.replace('&quot;','"')
    f=f.replace('&lt;','<')
    f=f.replace('&gt;','>')
    return f
for i in os.listdir(os.getcwd()):
    if i!='change.py':
        fp=open(i,'r',encoding='utf-8')
        data=fp.read()
        data=turn(data)
        fp.close()
        fp=open(i,'w',encoding='utf-8')
        fp.write(data)
        fp.close()
        
