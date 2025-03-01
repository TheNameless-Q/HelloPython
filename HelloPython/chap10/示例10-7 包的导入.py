
#(1)
import admin.my_admin as a # import 包名.模块名 as 别名
print('-'*50)
#上述代码的执行结果证明，当包被导入时，__init__.py中的代码自动被调用执行
a.info()
print('-'*50)

#(2)
from admin import my_admin as b
b.info()#包被导入时，__init_.py自动执行且只执行一次
print('-'*50)

#(3)
from admin.my_admin import info
info()
print('-'*50)

#(4)
from admin.my_admin import *
print(name,age)
info()




