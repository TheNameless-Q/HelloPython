import my_info
print(my_info.name)
print(my_info.age)
print(my_info.info())
print('-'*50)

#(2)
import my_info as a
print(a.name)
print(a.age)
print(a.info())
print('-'*50)

#(3)
from my_info import name
print(name)

from my_info import info
info()

from my_info import * # 通配符*
print(name,age)

#(4)同时导入多个模块
import math,time,random



