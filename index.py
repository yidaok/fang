import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import Series
import jieba
import matplotlib.pylab as plt
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )



path = r"C:\Users\sunnan\Desktop\JFpinglun.xlsx"
name = ['appltnum','city','agentmail','agentname','marks','notes','notetime','fangkuantime','username','usertel','inoroutnum','inorout','isfollow']
df = pd.read_excel(path,names=name)

# fenci
# notelist_cut = []
# lists = []
# notelist = df.ix[:,'notes'].dropna()
# for i in notelist:
#     jiebas = jieba.cut(str(i),cut_all=False)
#     for ii in jiebas:
#         lists.append(ii)
#
# with open(r"C:\Users\sunnan\Desktop\txt.txt",mode='w') as fb:
#     for i in lists:
#         fb.write(i+'\n')
#     fb.close()


# pingfen
# mark = df.ix[:,'marks']
# print mark.value_counts()




