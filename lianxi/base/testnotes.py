# def f(hams: str, eggs: str = 'eggs') -> str:
#     print("Annotations:", f.__annotations__)
#     print("Arguments:", hams, eggs)
#     return hams + 'and' + eggs
#
#
# f('test')
# f('test', 'aaa')


def append_item(item, list1=[]):
    if list1 is not None:
        list1 = []

    # if list1 is not []:
    #     list1 = []
    # if  [1]:
    #     list1 =[11]
    #     print('hahah')

    # if list1 == [1]:
    #     list1=[11]

    list1.append(item)
    return list1


print(append_item(0))
print(append_item(1))
print(append_item(2))
