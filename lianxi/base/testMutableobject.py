a1 = [1, 2, 3]
a2 = a1
print(id(a1), id(a2))
a2 = a2 + [4] # 这个等式中，右边的a2还是和a1的id一样的，一旦赋值成功，a2就指向新的对象
print(id(a1), id(a2))  # 不等，a2的id变化了
print(a1) # [1, 2, 3]没有变

print('-------------------------------')

a1 = [1, 2, 3]
a2 = a1
print(id(a1), id(a2))
a2 += [4]  # 相当于调用了a2.extend([4]),原地改变并没有新的对象产生
print(id(a1), id(a2))  # 相等，a2的id没有变化
print(a1)