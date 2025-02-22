#三行四列长方形
for i in range(1,4):# 外层循环--行
    for j in range(1,5):# 内层循环--列
        print('*',end='')# 每行的*号之间不换行
    print()# 打印完每行后换行

print('-'*40)

# 直角三角形
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    print()

