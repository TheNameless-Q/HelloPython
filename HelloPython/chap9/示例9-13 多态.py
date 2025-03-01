class Person():
    def eat(self):
        print('人，吃五谷杂粮')

class Cat():
    def eat(self):
        print('猫，喜欢吃鱼')

class Dog():
    def eat(self):
        print('狗，喜欢啃骨头')
#定义一个函数，传入参数的类型是我们所不确定的也不关心的，但只要它具有eat方法就可以；
#这就是多态：不关心数据类型，只关心同名的方法
def fun(obj):
    obj.eat()

#创建对象
per=Person()
cat=Cat()
dog=Dog()

#调用函数fun
fun(per)
fun(cat)
fun(dog)