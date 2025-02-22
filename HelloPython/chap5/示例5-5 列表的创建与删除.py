lst1=['hello','world',98,10.5]
print(lst1)

lst2=list('Hello World')
print(lst2)

lst3=list(range(1,10,2))
print(lst3)

# 列表是序列的一种，对序列的操作均可应用到列表
print(lst1+lst2+lst3)
print(lst3*3)
print(max(lst3))
print(min(lst3))
#......

# 列表的删除操作
lst4=[10,20,30]
print(lst4)

del lst4
#print(lst4)# 删除后再输出就会报错：lst4未定义


