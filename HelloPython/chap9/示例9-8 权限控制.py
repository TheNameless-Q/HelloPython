class Student():
    def __init__(self,name,age,gender):
        self._name=name# _name单下划线开头，受保护的，仅能本类和子类访问（但实际上也可为外部访问，属于是防君子不防小人）
        self.__age=age# __age双下划线开头，表示private，仅能类本身访问
        self.gender=gender# 普通的实例属性，类的内部、外部和子类都可以访问

    def _fun1(self):#受保护的
        print('我是一个受保护的实例方法，仅能本类和子类访问')

    def __fun2(self):
        print('我是一个私有的实例方法，双下划线开头，表示private，仅能类本身访问')

    def show(self):# 普通的实例方法
        self._fun1()
        self.__fun2()
        print(self._name)
        print(self.__age)

#创建学生对象
stu=Student('wyl',22,'male')

#类的外部调用属性
print(stu._name)
# print(stu.__age)#AttributeError: 'Student' object has no attribute '__age'. Did you mean: '_name'?
                  #意味着私有的属性在类的外部不可使用

#类的外部调用方法
stu._fun1()
# stu.__fun2()#私有方法在类之外不可访问

#私有属性和私有方法真的不能在类之外访问嘛？【n】
print(stu._Student__age)
stu._Student__fun2()
print('-'*50)

#为什么可以使用上述的形式访问私有属性和私有方法？
print(dir(stu))#'_Student__age', '_Student__fun2' 私有属性和私有方法在内部被定义为扩展的名字