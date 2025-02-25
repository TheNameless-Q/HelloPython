# 创建一个列表，循环五次以模拟往购物车中放入五件物品
lst=[]
for i in range(5):
    goods=input('请输入商品的编号和名称进行商品入库，每次只能输入一件物品：')
    lst.append(goods)

# 输出所有的商品信息
for item in lst:
    print(item)

cart=[]
while True:
    flag=False # 代表没有商品的情况
    num=input('请输入要购买的商品的编号：')
    # 遍历商品列表，查询要购买的商品是否存在
    for item in lst:
        if num==item[0:4]:#切片操作，从商品信息中取出编号
            flag=True # 代表商品已找到
            cart.append(item)
            print('商品已成功添加到购物车！')
            break
    if not flag and num!='q':
            print('商品不存在！')
    if num=='q':
        break# 退出while循环
print('-'*40)
print('已添加到购物车里的商品为：')
cart.reverse()
for item in cart:
    print(item)









