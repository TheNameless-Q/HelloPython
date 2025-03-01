class A():
    pass

class B():
    pass

class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age

a=A()
b=B()
c=C('wyl',22)

print('对象a的属性字典：',a.__dict__)
print('对象b的属性字典：',b.__dict__)
print('对象c的属性字典：',c.__dict__)

print('对象a所属的类：',a.__class__)
print('对象b所属的类：',b.__class__)
print('对象c所属的类：',c.__class__)

print('A类的层次结构：',A.__mro__)
print('B类的层次结构：',B.__mro__)
print('C类的层次结构：',C.__mro__)#C类首先继承了A类、B类，又间接继承了object类（爷爷类）
