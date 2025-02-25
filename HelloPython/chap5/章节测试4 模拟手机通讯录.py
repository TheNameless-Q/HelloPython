# 创建一个空集合
s=set()
for i in range(1,6):
    info=input(f'请输入第{i}好友的姓名和手机号：')#f 前缀用于定义一个格式化字符串,允许你在字符串中直接嵌入表达式，这些表达式会被它们的值所替换
    # 将上述info添加到s集合中
    s.add(info)
# 遍历输出
for item in s:
    print(item)









