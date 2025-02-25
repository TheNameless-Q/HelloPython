# 大小写转换
s1='HelloWorld'
s2=s1.lower()
s3=s1.upper()
print(s1,s2,s3)

# 字符串的分隔
e_mail='wyl@126.com'
lst=e_mail.split('@')
print('邮箱名：',lst[0],'域名：',lst[1])

# 统计子串在字符串中出现的次数
print(s1.count('o'))

# 检索操作
print(s1.find('o'))#o在字符串s1中首次出现的索引
print(s1.find('p'))#不存在时，返回-1，代表没有找到
print(s1.index('o'))
#print(s1.index('p'))# ValueError: substring not found

# 判断前缀和后缀
print(s1.startswith('H'))
print(s1.startswith('W'))

print('demo1.py'.endswith('.py'))# True，表示它是一个python文件
print('text.txt'.endswith('.txt'))
