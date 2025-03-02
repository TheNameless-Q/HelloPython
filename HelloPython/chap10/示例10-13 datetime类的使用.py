from datetime import datetime #从datetime模块中导入datetime类
dt=datetime.now()
print(dt)#2025-03-02 18:01:48.201823

dt2=datetime(2028,10,25,20,12,8)
print('dt2的数据类型:',type(dt2))
print('dt2所表示的日期时间：',dt2)
print('年：',dt2.year,'月：',dt2.month,'日：',dt2.day)
print('-'*50)

#比较两个datetime类型对象的大小
labor_day=datetime(2028,5,1)
national_day=datetime(2028,10,1)
print('劳动节比国庆节早吗？',labor_day<national_day)

#datetime类型与字符串类型进行转换
nowdt=datetime.now()
nowdt_str=nowdt.strftime('%Y-%m-%d %H:%M:%S')
print('nowdt的数据类型：',type(nowdt),'nowdt所表示的时间：',nowdt)
print('nowdt_str的数据类型：',type(nowdt_str),'nowdt_str所表示的时间：',nowdt_str)
print('-'*50)

#字符串类型转换为datetime类型
str_datetime='2028年8月8日 20点15分'
dt3=datetime.strptime(str_datetime,'%Y年%m月%d日 %H点%M分')
print('str_datetime的数据类型',type(str_datetime),'str_datetime所表示的时间',str_datetime)
print('dt3的数据类型',type(dt3),'dt3所表示的时间',dt3)