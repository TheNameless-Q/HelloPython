d={1000:'张三',1001:'李四',1002:'王五'}
print(d)

# 向字典中添加元素
d[1003]='李华'
print(d)

# 获取字典中所有的键
keys=d.keys()
print(keys)#dict_keys([1000, 1001, 1002, 1003])--获取一个对象dict_keys
print(list(keys))#转换为列表查看对象的内容
print(tuple(keys))#转换为元组查看对象的内容

# 获取字典中所有的值
values=d.values()
print(values)#dict_values(['张三', '李四', '王五', '李华'])--获取一个对象dict_values
print(list(values))
print(tuple(values))

# 将字典中的数据转换为key-value形式，以元组的方式进行输出
lst=list(d.items())
print(lst)#[(1000, '张三'), (1001, '李四'), (1002, '王五'), (1003, '李华')]--整体是一个列表，列表每一个元素是元组

d=dict(lst)
print(d)

# 使用pop函数
print(d.pop(1001))
print(d)

print(d.pop(1008,'不存在'))
print(d)

# 使用popitem函数进行随机删除
print(d.popitem())
print(d)

# 清空字典中的所有元素
d.clear()
print(d)

# python中一切皆对象，每个对象都有一个布尔值
print(bool(d))


