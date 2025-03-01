a=10
b=20
print(a+b)

#查看对象a的全部属性和方法
print(dir(a))
#调用特殊方法实现a和b相加
print(a.__add__(b))

