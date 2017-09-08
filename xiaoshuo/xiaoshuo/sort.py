# -*- coding: utf-8 -*-
import csv
import pandas as pd
import numpy as np
import sys
reload(sys)
# sys.setdefaultencoding('utf-8')
sys.setdefaultencoding('utf_8_sig')

#filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，header=None表示头部为空，
# sep=' '表示数据间使用空格作为分隔符，如果分隔符是逗号，只需换成 ‘，’即可。
# df=pd.read_csv('/Users/shiqingwang/Desktop/code/python/github/Python/xiaoshuo/xiaoshuo/dingdian.csv') 
# df=pd.read_csv('dingdian.csv')
# df=pd.read_csv('items.csv',names=['novel_name','category','collects','reviews'])
# print df.head()
# print df.tail()#作为示例，输出CSV文件的前5行和最后5行，这是pandas默认的输出5行，# 可以根据需要自己设定输出几行的值
# cols = df.columns # 返回全部列名
# print cols
# df = pd.read_csv('items.csv',header=0)
# df = pd.read_csv('xxsy.csv',header=0)
df = pd.read_csv('xiaoshuo2.csv',header=0)
# df = pd.read_csv('xs.csv',header=0)
# print df.head()
# print ""
lc=pd.DataFrame(df)
# asc升序
# axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last', sort_remaining=True, by=None
# new = lc.sort_index(by="collects",ascending=False)
new = lc.sort_values(by=['reviews','collects'],ascending=False)
# # # new = lc.nlargest(5,['collects'])
print new.head(10)
# df2=pd.DataFrame(df).nlargest(5, columns='collects')
# print df2
# new = lc.sort_values(by=['reviews'],ascending=False)
# print new.head(10)

# leetcode
# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         looktable = {}
#         for i, v in enumerate(nums):
#             print looktable;
#             if target - v in looktable:
#                 return [looktable[target-v], i]
#             looktable[v] = i

# test = Solution()
# nums = [3,2,4]
# test.twoSum(nums,6)

