class Student():
    #类属性：定义在类之中、方法外的变量
    school='北京XXX教育'

    #实例属性：定义在__init__方法（初始化方法）中，self打点的变量
    def __init__(self,xm,age):#xm|age都是初始化方法的参数，是局部变量，作用域仅限于当前方法
        self.name=xm# =左侧self.name是实例属性，右侧xm是局部变量，=执行赋值操作
        self.age=age# 实例属性和局部变量的名称可以相同
