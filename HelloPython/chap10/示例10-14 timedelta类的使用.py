from datetime import timedelta
from datetime import datetime
#通过两个datetime对象相减的方式创建timedelta类型的对象
delta1=datetime(2028,10,1)-datetime(2028,5,1)
print('delta1的数据类型：',type(delta1),'delta1所表示的时间：',delta1)
print('2028年5月1日后的153天是：',datetime(2028,5,1)+delta1)
print('-'*50)

#通过传入参数的方式创建一个timedelta类型的对象
td1=timedelta(10)
print(td1)