lst=[3,1,24,27,55,89]
print('原列表：',lst,id(lst))
lst2=sorted(lst)
print('原列表：',lst,id(lst))
print('写列表：',lst2,id(lst2))
lst3=sorted(lst,reverse=True)
print('降序排序：',lst3,id(lst3))

print('-'*40)
lst4=['Banana','apple','orange','Cat']
print('原列表：',lst4,id(lst4))
lst5=sorted(lst4,key=str.lower)
print('忽略大小写排序：',lst5,id(lst5))





