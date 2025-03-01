class Student():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.__gender=gender

    #使用@property 修改方法，将方法转换为属性使用
    @property
    def get_gender(self):
        return self.__gender

    #将gender这个属性设置为可写属性
    @get_gender.setter
    def get_gender(self,gender):
        if gender!='女' and gender!='女':
            print('性别设置有误，已将性别默认为男')
            self.__gender='男'
        else:
            self.__gender=gender

stu=Student('wyl',22,'男')
print(f'我叫{stu.name}，我的性别为{stu.get_gender}')
print('-'*50)

#修改私有属性gender
stu.get_gender='其他'
print(stu.get_gender)