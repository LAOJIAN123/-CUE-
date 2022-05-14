from asyncio.windows_events import NULL
import os
import re
import random
import numpy as np
from numpy import *
#正则表达式  
#[^\\]*.\.cue$    提取文件名
def change_to_flac(path):
    list=[]
    for root,dirs,files in os.walk(path):
        #root为当前访问文件夹路径
        #dirs为当前文件夹内的子目录名list
        #files表示文件夹下的文件list
        for f in files:
            data = os.path.join(root,f)                                                                             #data为存放索引到的文件目录  
            matchObj = re.search(r'.cue$',f)                                                                        #提取文件名的正则表达式
            if matchObj != None:
                list.append(data)    
                # print(data)   
    
    for Obj in list:
        Obj = re.sub("\\\\","/",Obj)
        try:                                                                                                        #将每个cue文件操作
            with open(Obj,'r',encoding='utf-8') as Cue_file1,open(Obj+r".dat",'w',encoding='utf-8') as Cue_file2:   #创建出读取文件Cue_file1对象，和写入文件的Cue_file2对象
                for text01 in Cue_file1:
                    Cue_file2.write(re.sub(r'.tak" WAVE',r'.flac" WAVE',text01))                                    #resub(1,2,text01) 1:替换前文本 2：替换后文本
            os.remove(Obj)
            os.rename(Obj+r".dat",Obj)
        except Exception as result:#异常处理
            print("发生错误：",result)
            Cue_file1.close()
            Cue_file2.close() 


path01 = r'C:\Users\10466\Desktop\K-ON!\K-ON!'                                                                       #需要修改内容的目录
change_to_flac(path01)