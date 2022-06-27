# -*- coding:utf-8 -*-
# @TIME : 2022/6/26 21:21
# @Author : killy
# @File : day01.py

import re

'''这是第一天的学习内容'''

# 1.匹配出163的邮箱地址，且@符号之前有4到20位，例如hello@163.com
res1 = re.match('[a-zA-Z0-9_]{4,20}@(163|qq|126)\.com', 'hello@163.com')
# print(res1.group())
# 2.匹配出11位手机号码
res2 = re.match('\d{11}', '13346667349')
print(res2.group())
# 3.匹配出微博中的话题, 比如: #幸福是奋斗出来的#
# res3 = re.match('[#]{1}\w{1,}[#]{1}', '#幸福是奋斗出来的#')
res3 = re.match('\W\w{1,}\W', '#幸福是奋斗出来的#')
# print(res3.group())
