lst=['hello','world','python','php']
# 使用遍历循环for遍历列表元素
for item in lst:
    print(item)
print('-'*40)


# 使用for循环、range函数、len()函数，根据索引遍历列表元素
for i in range(0,len(lst)):
    print(i,'-->',lst[i])
print('-'*40)


# 第三种遍历方式 enumerate函数
for index,item in enumerate(lst):
    print(index,'-->',item)# 强调，此处index是序号而非索引，可以手动修改序号的初始值

for index,item in enumerate(lst,start=1):
    print(index,'-->',item)