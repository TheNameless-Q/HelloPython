lst=['hello','world','python']
print('原列表：',lst,id(lst))
# 增加列表元素的操作
lst.append('sql')
print('增加元素之后的列表：',lst,id(lst))

# 插入操作
lst.insert(1,'100')
print('插入后的列表：',lst,id(lst))

# 列表元素的删除操作
lst.remove('world')
print('删除元素之后的列表',lst,id(lst))

# pop
lst.pop(1)
print('pop后的列表：',lst,id(lst))

# 清除列表中所有的元素clear
# lst.clear()
# print(lst,id(lst))

# 列表的逆序输出
lst.reverse()
print(lst,id(lst))

 # 列表的拷贝copy
new_lst=lst.copy()
print('原列表：',lst,id(lst))
print('拷贝生成的新列表：',new_lst,id(new_lst))

# 列表元素的修改
# 根据索引修改对应元素
lst[1]='happy'
print(lst)






