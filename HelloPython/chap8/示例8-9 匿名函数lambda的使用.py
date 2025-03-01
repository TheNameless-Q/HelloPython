def calc(a,b):
    return a+b

print(calc(1,2))
print('-'*50)
s=lambda a,b:a+b
print(type(s))
print(s(1,2))
print('-'*50)

# lambda函数用于列表取值
lst=[10,20,30,40,50]
for i in range(len(lst)):
    print(lst[i])
print('-'*20)
for i in range(len(lst)):
    result=lambda x:x[i]
    print(result(lst))
print('-'*50)

# lambda函数用于字典排序
student_scores=[
    {'name':'zhangsan','score':80},
    {'name':'lisi','score':90},
    {'name':'wangwu','score':85},
    {'name':'wyl','score':100},
]
student_scores.sort(key=lambda x:x.get('score'),reverse=True)
print(student_scores)



