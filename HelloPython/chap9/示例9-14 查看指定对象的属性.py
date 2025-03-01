class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'我叫{self.name}，我今年{self.age}岁了')

per=Person('wyl',22)#在创建对象时，由系统自动调用了__init__(self,name,age)方法
per.show()

print(dir(per))#查看per对象所有具有的全部属性（包含方法），除却name,age,show都是源自object类
print(per)#<__main__.Person object at 0x000001AB9B841550>  与__str__方法有关

