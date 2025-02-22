import random
lst=[item for item in range(1,11)]
print(lst)

lst2=[item**2 for item in range(1,11)]
print(lst2)

lst3=[random.randint(1,100) for _ in range(10)]
print(lst3)

#从列表中选择符合条件的元素组成新的列表
lst4=[i for i in range(1,11) if i%2==0]
print(lst4)