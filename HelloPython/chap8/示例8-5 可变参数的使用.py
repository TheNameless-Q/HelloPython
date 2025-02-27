def fun(*para):# 个数可变的位置参数
    print(type(para))
    for item in para:
        print(item)

# 调用
fun(10,20,30)
fun(10)
fun(20,30)
fun([11,22,33,44])
# 在调用时，参数前加一颗星，将对列表解包
fun(*[11,22,33,44])

print('-'*50)
# 个数可变的关键字参数
def fun2(**kwpara):
    print(type(kwpara))
    for key,value in kwpara.items():
        print(key,'---',value)

# 调用
fun2(name='wyl',age=18,gender='male')
d={'name':'qkc','age':18,'gender':'male'}
# fun2(d)直接用字典作为参数是不正确的
fun2(**d)# 用双**对字典进行解包

