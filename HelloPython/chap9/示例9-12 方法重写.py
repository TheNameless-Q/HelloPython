class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f'我叫{self.name},我今年{self.age}岁了')

class Student(Person):
    def __init__(self,name,age,num):
        super().__init__(name,age)
        self.num = num

    def show(self):
        #super().show()
        print(f'我叫{self.name},我今年{self.age}岁了,我的学号是{self.num}')



class Doctor(Person):
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.department = department

    def show(self):
        print(f'我叫{self.name},我今年{self.age}岁了,我是{self.department}部门的')

# 创建子类对象
stu=Student('wyl',22,'1001')
stu.show()
doc=Doctor('qkc',32,'外科')
doc.show()