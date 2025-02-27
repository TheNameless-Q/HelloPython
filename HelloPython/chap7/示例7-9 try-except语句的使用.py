try:
    num1=int(input('请输入一个整数作为被除数：'))
    num2=int(input('请输入另一个整数作为除数：'))
    result=num1/num2
    print('结果=',result)
except ZeroDivisionError:
    print('除数为0')