# 返回一个可迭代对象
print(range(5))


for i in range(1,10,3):
    print(i)


list1=list(range(0))
list2=list(range(0,1))
list3=list(range(1,0))
list4=list(range(1,10,3))
print('list1是:'list1)
print('list2是:'list2)
print('list3是:'list3)
print('list4是:'list4)