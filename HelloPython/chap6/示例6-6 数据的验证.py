# isdigit() 十进制的阿拉伯数字
print('123'.isdigit())# True
print('一二三'.isdigit())# False
print('0b1010110'.isdigit())# False
print('ⅢⅢⅢ'.isdigit())# False
print('-'*50)

# isnumeric() 所有字符都是数字
print('123'.isnumeric())# True
print('一二三'.isnumeric())# True
print('0b1010110'.isnumeric())# False #？？？
print('ⅢⅢⅢ'.isnumeric())# True
print('零壹贰'.isnumeric())# True
print('-'*50)

# isalpha() 所有字符都是字母（既包含英文字母也包含中文字母）
print('hello世界'.isalpha())# True
print('hello世界123'.isalpha())# False，因为存在数字123
print('hello世界一二三'.isalpha())# True
print('hello世界ⅢⅢⅢ'.isalpha())# True
print('-'*50)

# isalnum() 所有字符都是数字或字母
print('hello世界'.isalnum())# True
print('hello世界123'.isalnum())# True
print('-'*50)

# 判断字符串的大小写
print('HelloWorld'.islower())# False
print('HELLOWORLD'.isupper())# True
print('hello世界'.islower())# True
print('HELLO世界'.isupper())# True-->认为中文既是大写也是小写
print('-'*50)

# istitle() 如果字符串是标题化的
#...

# isspace() 如果都是空白字符
#...






