d={'hello':10,'world':20,'happy':30}
# 访问字典中的元素
#（1）使用d[key]
print(d['hello'])

#（2）使用d.get(key)
print(d.get('hello'))

# 上述二者存在区别，如果d[key]的key不存在则会报错，而d.get(key)可以指定默认值
# print(d['java'])#报错
print(d.get('java'))#没有，输出默认值None
print(d.get('java','不存在'))# 指定不存在时的输出信息


# 字典的遍历
for item in d.items():
    print(item,type(item))#有key和value组成的元组

# 在使用for循环遍历时，分别获取key和value
for key,value in d.items():
    print(key,'-->',value)

