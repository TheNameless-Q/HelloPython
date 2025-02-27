s='伟大的中国梦'
# 编码：str->bytes
s_encoded=s.encode(errors='replace')# 不指明编码方式时，默认位UTF-8编码方式，因为UTF-8编码中一个中文占三个字节
print(s_encoded)

s_encoded_GBK=s.encode('gbk',errors='replace')#GBK中一个中文占两个字节
print(s_encoded_GBK)


# 编码中的出错问题
s2='🔺哈哈哈'
s2_encoded=s2.encode('gbk',errors='ignore')# 'ignore'忽略了出错的🔺，因此编码输出结果仅含有'哈哈哈'的编码
print(s2_encoded)

# s2_encoded2=s2.encode('gbk',errors='strict')# strict意为严格的，因此遇到编码错误直接报错而不会忽略
# print(s2_encoded)

s2_encoded3=s2.encode('gbk','replace')
print(s2_encoded3)

# 解码类型 bytes->str
print(bytes.decode(s_encoded,'utf-8'))
print(bytes.decode(s_encoded_GBK,'gbk'))
print(bytes.decode(s2_encoded,'gbk'))

