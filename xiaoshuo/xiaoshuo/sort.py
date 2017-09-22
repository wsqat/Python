# -*- coding: utf-8 -*-
import csv
import pandas as pd
import numpy as np
import sys
reload(sys)
# sys.setdefaultencoding('utf-8')
sys.setdefaultencoding('utf_8_sig')

df = pd.read_csv('novels.csv',header=0,usecols=[0,1,6,7,8])
# df.iloc[:,[0,1]]
# print df.head()
#cols = df.columns
#print cols

# 本月点击排行榜，
lc=pd.DataFrame(df)
lc = lc.iloc[:,[0,4]]
# print df.columns
# print lc.head()
new = lc.sort_values(by=['month'],ascending=True)
new = new.tail(20)
# print new.shape
# print new.columns

import matplotlib.pyplot as plt
plt.rcdefaults()
# present = new.set_index('novel_name')
# present[:20].plot(kind='barh')
# # plt.figure(figsize=(12,9))
# plt.title(u'热门小说本月点击排行榜', fontsize=16)
# plt.xlabel(u'热门小说本月点击量', fontsize=16)
# plt.ylabel(u'热门小说名称', fontsize=16)
# plt.show()

# 历史点击排行榜，
lc2 = pd.DataFrame(df)
lc2 = lc2.iloc[:,[0,3]]
new2 = lc2.sort_values(by=['reviews'],ascending=True)
# new2 = new2.tail(20)
# present = new2.set_index('novel_name')
# present[:20].plot(kind='barh')
# plt.title(u'热门小说历史点击排行榜', fontsize=16)
# plt.xlabel(u'热门小说历史点击量', fontsize=16)
# plt.ylabel(u'热门小说名称', fontsize=16)
# plt.show()

# 历史收藏榜，
# lc3 = pd.DataFrame(df)
# lc3 = lc3.iloc[:,[0,2]]
# new3 = lc3.sort_values(by=['collects'],ascending=True)
# new3 = new3.tail(20)
# present = new3.set_index('novel_name')
# present[:20].plot(kind='barh')
# plt.title(u'热门小说历史收藏榜', fontsize=16)
# plt.xlabel(u'热门小说历史收藏量', fontsize=16)
# plt.ylabel(u'热门小说名称', fontsize=16)
# plt.show()

# 热门作者，
lc4 = pd.DataFrame(df)
lc4 = lc4.iloc[:,[1,3]]
lc4 = lc4.groupby(by=['author'])['reviews'].sum()
# 生成的数据类型是Series,如果进一步需要将其转换为dataframe,可以调用Series中的to_frame()方法.
lc4 = lc4.to_frame()
new4 = lc4.sort_values(by=['reviews'],ascending=False)
new4 = new4.head(20)
print new4
# present = new4.set_index('author')
# present[:20].plot(kind='barh')
# plt.title(u'热门小说作者排行榜', fontsize=16)
# plt.xlabel(u'热门小说作者点击量', fontsize=16)
# plt.ylabel(u'热门小说作者', fontsize=16)
# plt.show()

