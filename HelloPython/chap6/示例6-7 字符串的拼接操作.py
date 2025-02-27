s1='hello'
s2='world'
#(1)
print(s1+s2)
print('-'*50)

#(2)
print(''.join([s1,s2]))
print('*'.join(['C++','Java','Python','php']))
print('-'*50)

#(3)直接拼接
print('hello''world')
print('-'*50)

#(4)使用格式化字符串进行拼接
print('%s%s' % (s1,s2))
print(f'{s1}{s2}')
print('{0}{1}'.format(s1,s2))