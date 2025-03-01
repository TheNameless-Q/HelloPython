
#定义Student类
class Student():
    #类属性：定义在类之中、方法外的变量
    school='北京XXX教育'

    #实例属性：定义在__init__方法（初始化方法）中，self打点的变量
    def __init__(self,xm,age):#xm|age都是初始化方法的参数，是局部变量，作用域仅限于当前方法
        self.name=xm# =左侧self.name是实例属性，右侧xm是局部变量，=执行赋值操作
        self.age=age# 实例属性和局部变量的名称可以相同

    #实例方法：定义在类之中的函数，自带参数self
    def show(self):
        print(f'我叫{self.name}，我今年{self.age}岁了')

    #静态方法：使用装饰器@staticmethod修饰的方法
    @staticmethod
    def sm():#静态方法不会自带self；写就有，不写就没有
        #print(self.name)
        #self.show()
        print('这是一个静态方法，且没写self参数，因此不能使用实例属性和实例方法')

    #类方法：使用装饰器@classmethod修饰的方法
    @classmethod
    def cm(cls):#类方法自带cls参数，它是class的缩写
        #print(self.name)
        #self.show
        print('这是一个类方法，且没写self参数，因此不能使用实例属性和实例方法')

#创建4个学生对象
stu=Student('wyl',18)
stu2=Student('qkc',19)
stu3=Student('马冬梅',20)
stu4=Student('zhangsan',22)

print(type(stu))
print(type(stu2))
print(type(stu3))
print(type(stu4))#<class '__main__.Student'>
print('-'*50)
print(Student.school)
Student.school='原神大学'#类属性可修改？或者默认为public
print(Student.school)
print('-'*50)

#将4个学生对象存储到列表中
lst=[stu,stu2,stu3,stu4]
for item in lst:
    item.show()


