def printinfo(name, age=15):
    print('名字是：' + name + ',年龄是:' + str(age))


# printinfo('xiaoming', age='16')
#
# printinfo('xiaoli')

printinfo('xiaoli')

printinfo('xiaoming', age='16')


def changelist(mylist):
    mylist.append([1,2,3,4,5])
    print('函数内mylist:',mylist)



mylist=[10,20,30]
changelist(mylist)
print('函数外mylist:',mylist)

list1=[1,2,3]
print(list1+[4])
list2=list1
print(id(list1),id(list2))