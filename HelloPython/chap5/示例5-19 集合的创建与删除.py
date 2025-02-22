#{}直接创建集合
from pickletools import string4

s={10,20,30,40,50}
print(s)

# 集合中只能存储不可变数据类型
# s={[10,20],[30,40]}#unhashable type: 'list'
# print(s)

# 使用set()创建集合
s=set()#空集合
print(s)

s={}#直接使用{}创建的是字典
print(s,type(s))#{} <class 'dict'>

s=set('helloWorld')
print(s,type(s))#{'e', 'o', 'r', 'd', 'l', 'h', 'W'} <class 'set'> 证明了集合是无序且不重复的

s2=set([1,2,3])
print(s2,type(s2))

s3=set(range(10))
print(s3,type(s3))

# 集合的删除
# del s3
# print(s3,type(s3))#name 's3' is not defined