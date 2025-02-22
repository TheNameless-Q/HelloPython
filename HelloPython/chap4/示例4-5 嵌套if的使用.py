answer=input('请问您喝酒了吗？（y/n）')
if answer=='y':
    proof=eval(input('请输入酒精含量：'))
    if proof<20:
        print('不构成酒驾，祝您一路平安！')
    elif proof<80:
        print('您已构成酒驾！')
    else:
        print('您已构成醉驾！')
else:
    print('您走吧！')