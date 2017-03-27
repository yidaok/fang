#coding:utf-8
import shutil
import os
import re

new_path = r"E:/gifs"
old_path = r"E:/gif2"

fb = os.listdir(old_path)
for i in fb:
    if re.match(r'\w*(.gif)',i):
        shutil.copy(old_path+r'/'+i,new_path)
        print 'success'
    else:
        pass