aa = ['A', 'B', 'C']
# 定义字典
a = {}
# 获取数组元素个数
num = len(aa)

for i in range(num):
    ia = aa[1]
    if i > 1:
        ia = aa[2]
    print(ia)
    a[aa[i]] = a.get(ia, 0) + 1
    # a[ia] = a.get(ia, 0) + 1
    print(a)

# cc = {'a':1,'b':2,'c':3}
# print(cc.get('a',0)+1)

# print(len(a))
# print(a.items())
# for key, value in a.items():
#     print("key=%s" % key)
