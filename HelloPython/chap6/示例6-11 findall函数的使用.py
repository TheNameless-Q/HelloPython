import re
pattern=r'\d\.\d+'
s='I study Python3.11 every day Python2.7 I love you'
s2='4.11 Python I study every day'
s3='Python I study every day'

match=re.findall(pattern,s)# 返回值是列表类型
print(match)
match2=re.findall(pattern,s2)
print(match2)
match3=re.findall(pattern,s3)
print(match3)
