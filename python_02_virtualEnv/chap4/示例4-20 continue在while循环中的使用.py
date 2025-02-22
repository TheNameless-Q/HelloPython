s=0
i=0
while i<=100:
    if i%2==1:
        i=i+1
        continue
    s=s+i
    i=i+1
print('0~100之间的偶数和=',s)
