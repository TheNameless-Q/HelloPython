s='HelloWorld'
# 字符串的替换
s1=s.replace('o', '你好')
s2=s.replace('o','你好',1)#第三个参数表示从前向后替换的次数，不写时默认全部替换
print(s1)
print(s2)

# 字符串在指定的宽度范围内居中
print(s.center(20))
print(s.center(20,'*'))

# 去除字符串左右的空格
s3='    Hello    World    '
print(s3.strip())# 去掉左右的空格
print(s3.lstrip())# 去掉左侧的空格 l-left
print(s3.rstrip())# 去掉右侧的空格


# 去掉指定的字符
s4='dl-HelloWorld'
print(s4)
print(s4.strip('ld'))# 与顺序无关，左右两侧只要包含'ld'中的字符就会被去掉
print(s4.lstrip('ld'))
print(s4.rstrip('ld'))



