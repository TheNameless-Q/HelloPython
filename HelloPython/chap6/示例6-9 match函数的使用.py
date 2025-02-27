import re # 导入re内置模块
pattern=r'\d\.\d+'# 匹配模式字符串 \d代表一个十进制数，等价于0~9；\.代表指定符号'.'，如果不加转移符号'\'，则代表除换行符\n外的任意单个字符；
                 # \d+由\d和+组成，表示一个或多个连续的十进制数
s='I study Python3.11 every day'# 待匹配字符串
match=re.match(pattern,s,re.I)#调用re模块内的match函数，用匹配模式字符串pattern匹配待匹配字符串s；re.I表示ignore;
print(match,type(match))# match是从起始位置开始匹配的，因此如果对应数据在中间就匹配不到
s2='3.11Python I study every day'
match2=re.match(pattern,s2)
print(match2)
print(type(match2))#返回值match是一个对象，因此具有它的一些方法;
print('-'*50)
print('匹配值的起始位置:',match2.start())
print('匹配值的结束位置:',match2.end())#匹配值的结束位置: 4 (不包含4)
print('匹配区间的位置元素:',match2.span())#
print('待匹配的字符串:',match2.string)
print('匹配的数据:',match2.group())