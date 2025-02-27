s='HelloWorld'
print(s)
print('{0:*<20}'.format(s))
print('{0:*>20}'.format(s))
print('{0:*^20}'.format(s))

# 居中对齐
print(s.center(20,'*'))

# 千位分隔符（只适用于整数和浮点数）
print('{0:,}'.format(987654321))
print('{0:,}'.format(987654321.1234))

# 浮点数精度
print('{0:.2f}'.format(3.1415926))

# 字符串的最大显示长度
print('{0:.5}'.format('HelloWorld'))

# 整数的不同进制
a=425
print('二进制:{0:b},十进制:{0:d},八进制:{0:o},十六进制:{0:x},十六进制:{0:X}'.format(a))

# 浮点数的科学计数法
b=3.1415926
print('{0:.2f},{0:.2E},{0:.2e},{0:.2%}'.format(b))








