luck_number=8;
my_name='王云立'

print('我的幸运数字是：',luck_number)
print('幸运数字的数据类型：',type(luck_number))

print('我的名字是：',my_name)
print('名字的数据类型是',type(my_name))

luck_number='北京欢迎你'
print('对luck_number重新赋值后幸运数字的数据类型：',type(luck_number))

# 在python中，允许多个变量指向同一个值
no=number=10
print(no,number)
print(id(no),id(number))

