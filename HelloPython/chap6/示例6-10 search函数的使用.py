import re
pattern=r'\d\.\d+'
s='I study Python3.11 every day Python2.7 I love you'
match=re.search(pattern,s)
print(match)

s2='4.11 Python I study every day'
match2=re.search(pattern,s2)
print(match2)

s3='Python I study every day'
match3=re.search(pattern,s3)
print(match3)

print(match2.group())
