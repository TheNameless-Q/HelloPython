# 创建字典用于存储车票信息，使用车次作为key，其他信息作为value
dict_ticket={
    'G1569':['北京南-天津南','18:06','18:39','00:33'],
    'G1567':['北京南-天津南','18:15','18:49','00:34'],
    'G8917':['北京南-天津西','18:20','19:19','00:59'],
    'G203':['北京南-天津南','18:35','19:09','00:34']
}
print('车次   出发站-到达站   出发时间   到达时间   历时时长')
# 遍历字典中的元素
for key in dict_ticket.keys():
    print(key,end='   ')
    # 根据key获取到的数据是一个列表
    for item in dict_ticket.get(key):# 根据key获取value
        print(item,end='   ')
    # 换行
    print()

# 输入用户的购票车次
train_num=input('请输入用户要购买的车次：')
# 根据key获取value
info=dict_ticket.get(train_num,'车次不存在')# 获取到的info是一个列表类型的数据
if info != '车次不存在':
    person=input('请输入乘车人，如果有多位乘车人以逗号分割：')
    # 获取车次的出发站-到达站，还有出发时间
    s=info[0]+' '+info[1]+'开'
    print('您已购买了'+train_num+' '+s+',请'+person+'尽快换取纸质车票。【铁路客服】')
else:
    print('对不起，您选择的车次不存在！')





