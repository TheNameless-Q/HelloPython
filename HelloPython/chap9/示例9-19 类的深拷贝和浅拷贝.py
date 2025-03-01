
class CPU():
    pass

class Disk():
    pass

class Computer():
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk

#创建对象
cpu=CPU()
disk=Disk()

#创建计算机对象
com=Computer(cpu, disk)

#对象的赋值（或称为变量的赋值）
com1=com
print(com,'子对象的内存地址：',com.cpu,com.disk)
print(com1,'子对象的内存地址：',com1.cpu,com1.disk)
#com和com1地址相同,意味着两者实际上是同一个对象
#子对象的内存地址也相同
#这意味着，无论是变量或对象的赋值，在实际的内存中都只有一个对象，对应一个地址，只不过"赋值"相当于起了多个名字
print('-'*50)

#类对象的浅拷贝
import copy
com2=copy.copy(com)
print(com,'子对象的内存地址：',com.cpu,com.disk)
print(com2,'子对象的内存地址：',com2.cpu,com2.disk)
#com com2的内存地址不同，意味着两者不是同一个对象，即copy.copy()创建了一个新的computer对象
#com com2的子对象内存地址相同，意味着两者的子对象是同一个
#这样的拷贝方式成为浅拷贝
print('-'*50)

#类的深拷贝
com3=copy.deepcopy(com)
print(com,'子对象的内存地址：',com.cpu,com.disk)
print(com3,'子对象的内存地址：',com3.cpu,com3.disk)
#com com3的内存地址不同，其子对象的内存地址也不同
#deepcopy创建了新的computer对象和子对象
#这种拷贝方式被称为深拷贝


