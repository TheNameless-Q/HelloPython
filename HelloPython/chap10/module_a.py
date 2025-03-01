# print('hello world')
# name='wyl'
# print(name) # 顶格写，为全局变量，被导入其他模块时自动执行这些代码

if __name__ == '__main__':
    print('hello world')
    name='wyl'
    print(name) # 将代码放进上述的语句格式中，则被导入其他模块时不会自动执行
