t=('happe','hello','world',10)
print(t[1])
print(t[0:3:2])

# 元组的遍历
for item in t:
    print(item,end='\t\t')
print()
# 索引的方式
for i in range(len(t)):
    print(i,t[i],end='\t\t')
print()

# enumerate函数
for index,item in enumerate(t):
    print(index,item,end='\t\t')
print()









