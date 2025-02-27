def happy_birthday(name,age):
    print(f'祝{name}{age}岁生日快乐！')

happy_birthday(age='18',name='wyl')
# 关键字传参和位置传参可以一起使用但不建议；
# 如果非要使用务必保证位置参数在前，关键字参数在后；
happy_birthday('wyl',age='18')