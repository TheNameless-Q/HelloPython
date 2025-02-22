import random
rand=random.randint(1,100)
count=1 #记录猜数的次数
while count<=10:
    number=eval(input('请输入您猜的数：'))
    if number==rand:
        print('猜对了！')
        break
    elif number>rand:
        print('您猜的数比真实数字大')
    else:
        print('您猜的数比真实数字小')
    count+=1
