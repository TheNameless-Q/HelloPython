import random
#设置随机数种子
random.seed(10)

#random.random()#x in the interval [0, 1)
print(random.random())
print(random.random())
print('-'*50)

#random.randint()#Return random integer in range [a, b], including both end points.
random.seed(10)
print(random.randint(1,100))
print('-'*50)

#random.randrange()#[m,n)步长为k:m->start=1,n->end=10,k->interval=3:从1、4、7中每次产生一个随机数
random.seed(10)
for i in range(10):
    print(random.randrange(1,10,3))
print('-'*50)

#random.rand

