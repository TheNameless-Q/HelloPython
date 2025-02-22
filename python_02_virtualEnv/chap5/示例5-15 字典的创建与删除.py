#(1)创建字典
d={10:'cat',20:'dog',30:'pet',20:'car'}# key相同时，后者的value覆盖前者的value
print(d)

#(2)zip函数
lst1=[10,20,30,40]
lst2=['cat','dog','pet','car']
d2=zip(lst1,lst2)
print(d2)#zip函数映射的结果是一个zip对象，需要特殊的方法查看
# d22=list(d2)#将zip对象转换为列表再输出
# print(d22,type(d22))
d222=dict(d2)#将zip对象转换为字典再输出;此时必须将上述list转换的语句注释掉；
print(d222,type(d222))

#(3)使用参数创建字典
d=dict(cat=10,dog=20,pet=30)#dict函数中，=左边是value，=右边是key
print(d)

t=(10,20,30)
print({t:10})#尝试用元组作key构成字典--可以

# lst=[10,20,30]
# print({lst:10})#报错，列表无hash，因此列表不能够作为key创建字典


# 字典仍属于序列
print('max:',max(d))
print('min:',min(d))
print('len:',len(d))

# 字典的删除
# del d
# print(d)#报错
