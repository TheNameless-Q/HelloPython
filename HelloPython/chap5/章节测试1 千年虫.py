lst=[88,89,90,98,00,99]
print(lst)

# #遍历列表的方式
# for index in range(len(lst)):
#     if lst[index]!=0:
#         lst[index]='19'+str(lst[index])
#     else:
#         lst[index]='200'+str(lst[index])
#
# print('修改后的列表：',lst)

# 使用enumerate函数
for index,value in enumerate(lst):
    if lst[index]!=0:
        lst[index]='19'+str(value)
    else:
        lst[index]='200'+str(value)
print('修改后的列表：',lst)