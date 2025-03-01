from my_info import *
from introduce import *
print(name)
print(age)#导入的不同模块具有相同名字的属性或方法，后导入的会覆盖先导入的

#不想令不同模块发生覆盖，解决方案：import导入再打点调用
import my_info
import introduce
print(my_info.name, my_info.age)
print(introduce.name, introduce.age)
