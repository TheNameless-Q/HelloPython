lst=[3,1,24,27,55,89]
print('原列表：',lst,id(lst))

# 对列表排序
lst.sort()# 默认是升序排序
print('升序排序后的列表：',lst,id(lst))

# 降序排序
lst.sort(reverse=True)
print('降序排序的列表：',lst,id(lst))

print('-'*40)

lst2=['Banana','apple','orange','Cat']
print('原列表：',lst2,id(lst2))
lst2.sort()# 按照ASCII码排序
print('升序排序后的列表：',lst2,id(lst2))

lst2.sort(reverse=True)
print('降序排序后的列表：',lst2,id(lst2))

print('-'*40)
# 忽略大小写排序
lst2.sort(key=str.lower)
print('忽略大小写排序：',lst2,id(lst2))
