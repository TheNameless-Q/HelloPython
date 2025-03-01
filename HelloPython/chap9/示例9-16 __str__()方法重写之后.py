class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "这是一个人类，具有名字和年龄两个实例属性"

    def show(self):
        print(f'我叫{self.name}，我今年{self.age}岁了')


per=Person('wyl',22)
print(per)#输出内存地址吗？不是

