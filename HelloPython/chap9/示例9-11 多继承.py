class FatherA():
    def __init__(self,name):
        self.name = name

    def showA(self):
        print('父类A的方法')

class FatherB():
    def __init__(self,age):
        self.age = age

    def showB(self):
        print('父类B中的方法')

class Son(FatherA,FatherB):
    def __init__(self,name,age,gender):
        FatherA.__init__(self,name)
        FatherB.__init__(self,age)
        self.gender = gender

son=Son('wyl',22,'男')
son.showA()
son.showB()