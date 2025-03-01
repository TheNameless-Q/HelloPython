lst=[11,9,22,77,57,50]
#(1)排序操作
asc_lst=sorted(lst)
desc_lst=sorted(lst,reverse=True)
print('原列表：',lst)
print('升序排序：',asc_lst)
print('降序排序:',desc_lst)
print('-'*50)

#(2)reversed 反向
new_lst=reversed(lst)
print(type(new_lst))#<class 'list_reverseiterator'> 迭代器对象，需要转换类型比如转成list类型才可显示输出
print(list(new_lst))
print('-'*50)

#(3)zip
x=['a','b','c','d']
y=[10,20,30,40,50]
zipobj=zip(x,y)
print(type(zipobj))#<class 'zip'>
print(dict(zipobj))
print('-'*50)

#(4)enumerate
enum=enumerate(y,start=1)
print(type(enum))#<class 'enumerate'>
print(tuple(enum))
print('-'*50)

#(5)all
lst2=[1,3,5,'',9]
print(all(lst))#True
print(all(lst2))#False
print('-'*50)

#(6)any
print(any(lst2))#True
print('-'*50)

#(7)next
zipobj2=zip(x,y)
print(type(zipobj2))#<class 'zip'>
print(next(zipobj2))#('a', 10)
print(next(zipobj2))#('b', 20)
print(next(zipobj2))#('c', 30)
print('-'*50)

#(8)filter
def fun(num):
    return num%2==1

filter_obj=filter(fun,range(10))
print(type(filter_obj))
print(list(filter_obj))
print('-'*50)

#(9)map
def upper(x):
    return x.upper()

lst3=['hello','python','world']
map_obj=map(upper,lst3)
print(type(map_obj))#<class 'map'>
print(list(map_obj))









