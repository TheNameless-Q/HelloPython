s={10,20,30}
s.add(100)
print(s)

s.remove(10)
print(s)

# s.clear()
# print(s)


# 集合的遍历操作
#(1)
for item in s:
    print(item)

#(2)
for index,item in enumerate(s):
    print(index,'-->',item)

# 集合的生成式
s={i for i in range(10)}
print(s)

s={i for i in range(10) if i%2==0}
print(s)