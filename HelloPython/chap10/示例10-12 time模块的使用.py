import time
now=time.time()
print(now)#1740908664.2041109 这就是一个时间戳，唯一对应当前的时间点
print(time.ctime())#时间戳所对应的已读字符串
print('-'*50)

obj=time.localtime()
print(obj)

obj2=time.localtime(60)
print(obj2)
print(type(obj2))
print('-'*50)

obj3=time.localtime(now)
print(obj3)
print('年份：',obj3.tm_year)
print('月份：',obj3.tm_mon)
print('日期：',obj3.tm_mday)
print('时：',obj3.tm_hour)
print('分：',obj3.tm_min)
print('秒：',obj3.tm_sec)
print('星期几：',obj3.tm_wday)#[0,6]:0->星期一；6->星期日
print('今年的第几天：',obj3.tm_yday)
print('-'*50)

#日期时间格式化
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))#str-字符串；f-format；
print('%B月份的名称：',time.strftime('%B',time.localtime()))
print('%A星期的名称：',time.strftime('%A',time.localtime()))
print('-'*50)

#休眠slepp()
time.sleep(10)
print('hello world')
