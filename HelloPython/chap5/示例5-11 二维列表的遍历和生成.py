#创建二维列表
lst=[
    ['城市','环比','同比'],
    ['北京',102,103],
    ['上海',104,504],
    ['深圳',100,39]
]
print(lst)

#遍历二维列表使用双重for循环
for row in lst:
    for item in row:
        print(item,end='\t\t')
    print()


#列表生成式 生成一个4行5列的二维列表
lst2=[[j for j in range(5)] for i in range(4)]
print(lst2)
