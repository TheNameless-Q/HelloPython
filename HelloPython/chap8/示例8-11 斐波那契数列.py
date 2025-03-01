def feibonaqi(n):
    if n==1 or n==2:
        return 1
    else:
        return feibonaqi(n-1)+feibonaqi(n-2)

for i in range(1,10):
    print(feibonaqi(i),end='\t')
print()

