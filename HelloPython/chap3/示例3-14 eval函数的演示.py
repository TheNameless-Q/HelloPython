S='3.14+3'
print(S,type(S))
x=eval(S)#使用eval函数去掉s这个字符串中左右的引号
print(x,type(x))


age=eval(input('请输入您的年龄：'))
print(age,type(age))