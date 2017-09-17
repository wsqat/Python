# -*- coding: utf-8 -*-
import csv
import pandas as pd
import numpy as np
import sys
reload(sys)
# sys.setdefaultencoding('utf-8')
sys.setdefaultencoding('utf_8_sig')

df = pd.read_csv('novel.csv',header=0,usecols=[0,1,6,7,8])
# df.iloc[:,[0,1]]
print df.head()
#cols = df.columns
#print cols

# 本月点击排行榜，
lc=pd.DataFrame(df)
lc = lc.iloc[:,[0,4]]
print df.columns
print lc.head()
new = lc.sort_values(by=['month'],ascending=False)
print new.head(20)

import matplotlib.pyplot as plt
plt.rcdefaults()
# print new.iloc[:,[1]].head()
# month = np.arange(len(new.iloc[:,[1]]))
# name = np.arange(len(new.iloc[:,[0]]))
# plt.bar(name, month, align='center', alpha=0.4)
# plt.xlabel(u'热门小说本月点击量')
# plt.ylabel(u'热门小说名称',fontproperties=getChineseFont())
# plt.title('热门小说本月点击排行榜')
# # plt.savefig("barh.eps",format="eps")
# plt.legend()
# # fig = plt.figure()
# plt.show()
# X = new.iloc[:,[1]].head(10)
# Y = new.iloc[:,[0]].head(10)
# month = np.arange(len(new.iloc[:,[1]]))
# name = np.arange(len(new.iloc[:,[0]]))

# lc.plot(kind='bar')  #分开并列线束
# lc.plot(kind='bar', stacked=True) #四个在同一个里面显示 百分比的形式
# new = new.head(20)
# # new.plot(kind='barh', stacked=False)#纵向显示
# plt.barh(month, name, 0.4, color="blue")
# # plt.barh(y_pos, performance, align='center', alpha=0.4)
# plt.yticks(new['month'], new['novel_name'])
# plt.xlabel(u'热门小说本月点击量')
# plt.ylabel(u'热门小说名称')
# plt.title(u'热门小说本月点击排行榜')
# plt.figure(figsize=(8,6), dpi=100)  # 创建一个8*6 点(point)的图，并设置分辨率为100
# # plt.show()

# 历史点击排行榜，
lc2 = pd.DataFrame(df)
lc2 = lc2.iloc[:,[0,3]]
new2 = lc2.sort_values(by=['reviews'],ascending=False)
print new2.head(20)

# 历史收藏榜，
lc3 = pd.DataFrame(df)
lc3 = lc3.iloc[:,[0,2]]
new3 = lc3.sort_values(by=['collects'],ascending=False)
print new3.head(20)

# 热门作者，
lc4 = pd.DataFrame(df)
lc4 = lc4.iloc[:,[1,3]]
new4 = lc4.sort_values(by=['reviews'],ascending=False)
print new4.head(20)

