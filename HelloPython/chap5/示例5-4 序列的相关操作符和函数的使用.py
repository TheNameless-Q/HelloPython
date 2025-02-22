s='HelloWorld'
# in 的使用
print('e在Hello World中存在吗？',('e' in s))
print('v在Hello World中存在吗？',('v' in s))

# not in 的使用
print('v在Hello World中存在吗？',(not('v' not in s)))

# 内置函数的使用
print('len():',len(s))
print('max():',max(s))# 此处是按照ASCII码计算大小的
print('min():',min(s))

# 序列对象的方法
print('s.index(e):',s.index('e'))
#print('s.index(v)',s.index('v'))# 不存在就会报错
print('s.count(e):',s.count('e'))
print('s.count(o):',s.count('o'))

