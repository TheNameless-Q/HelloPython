# 遍历字符串
for i in 'hello':
    print(i)

# range函数 产生一个[n,m)的整数序列，包含n但不包含m
for i in range(1,11):
    if i%2==0:
        print(i,'是偶数')

# 计算1~10的累加和
s=0 #创建容器，存储累加和
for i in range(1,11):
    s=s+i

print(s)

# 计算100~999之间的水仙花数
for i in range(100,1000):
    sd= i % 10
    tens= (i % 100) // 10
    hundred= i // 100
    if sd**3+tens**3+hundred**3==i:
        print(i,'是水仙花数')

