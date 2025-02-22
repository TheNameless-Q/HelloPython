# 使用小括号创建元组
t=('hello','world',[10,20,30],'python')
print(t)

# 使用tuple()创建元组
t2=tuple('helloWorld')
print(t2)

t3=tuple([10,20,30])
print(t3)

# 元组本质上属于序列，所以关于序列的操作都可以应用给元组


# 如果元组中仅有一个元素则逗号不能省略
t4=(10)
print(t4,type(t4))
t5=(10,)
print(t5,type(t5))

# 元组的删除
# del t5
# print(t5)




