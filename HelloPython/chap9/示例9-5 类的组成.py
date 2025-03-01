
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

#创建类的对象
stu=Student('wyl',18)#传入两个参数是因为__init__初始化方法含有(self,xm,age)一共3个形参，其中self是自带的无需手动传入，
                             # 因此只需要依次传入xm,age

#实例属性：使用对象名打点调用
print(stu.name,stu.age)

#类属性：使用类名打点调用
print(Student.school)

#实例方法：使用对象名打点调用
stu.show()

#类方法：使用类名打点调用
Student.cm()

#静态方法：使用类名打点调用
Student.sm()


