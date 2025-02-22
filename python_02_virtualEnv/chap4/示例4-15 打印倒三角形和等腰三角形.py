# 倒三角形
for i in range(1,6):
    for j in range(1,7-i):
        print('*',end='')
    print()


# 等腰三角形
'''
&&&&*
&&&***
&&*****
&*******
*********
只需将上述的&更改为空格即可
'''
for i in range(1,6):
    #打印倒三角空格
    for j in range(1,6-i):
        print(' ',end='')

    #打印等腰三角形
    for k in range(1,2*i):
        print('*',end='')

    #打印换行
    print()


