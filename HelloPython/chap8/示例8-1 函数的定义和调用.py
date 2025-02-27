# 累加和函数的定义
def get_sum(num):# 函数定义处的num为形式参数
    s=0
    for i in range(1,num+1):
        s=s+i
    print(f'1~{num}的累加和为：{s}')

# 函数的调用
get_sum(10)# 函数调用处的10为实际参数
get_sum(100)
get_sum(1000)
