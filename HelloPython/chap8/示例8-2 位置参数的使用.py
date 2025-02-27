def happy_birthday(name,age):
    print(f'祝{name}{age}岁生日快乐！')

# happy_birthday('wyl')# TypeError: happy_birthday() missing 1 required positional argument: 'age'
# happy_birthday(18,'wyl')# 实参顺序也应当和形参保持对应
happy_birthday('wyl',18)


