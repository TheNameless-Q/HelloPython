number=eval(input('请输入您的6位中奖号码：'))
if number==987654:
    print("恭喜您，中奖了！")
else:
    print('很遗憾，未中奖！')


print('-----------------------一种简化技巧--------------')
result='恭喜您中奖了！' if number==987654 else '很遗憾未中奖！'
print(result)