t=(i for i in range(10))
print('直接输出元组t：',t)
t=tuple(t)
print('将生成器对象转换为元组后再输出：',t)

# 遍历
# for item in t:
#     print(item)
# “遍历过一遍，因而对象中不存在元素了”？？？



# 下方代码未成功复现
# t=(i for i in range(1,4))
# print(t)
# print(t,__next__())





