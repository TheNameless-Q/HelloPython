s='helloworld'
# 切片操作
s1=s[0:5:2]
print(s1)

# 省略起始位置，则默认从0开始
s2=s[:5:2]
print(s2)

# 省略步长，则默认为1
s3=s[0:5]
print(s3)

# 省略结束位置，则默认包含最后一个元素
s4=s[0::1]
print(s4)

# 逆序输出
s5=s[::-1]# 等价于print(s[-1:-11:-1])
print(s5)
print(s[-1:-11:-1])

# 关于range函数
t1=range(10)
print(t1)