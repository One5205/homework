import json

j1=[{'name':'xiaoming','gender':'men','age':'15'},{'name':'xiaohong','gender':'women','age':'18'}]
j2='dad21'
print(json.dumps(j1))
#序列化，将python值转换为json格式的字符串
print(type(json.dumps(j1)))
print(j1[0]['name'])
print(json.dumps(j2))

j2='[{"name":"xiaoming","gender":"men","age":"15"},{"name":"xiaohong","gender":"women","age":"18"}]'
print(type(j2))
# 反序列化json.loads（），将json格式的字符串转换成python的数据类型
print(json.loads(j2))
print(type(json.loads(j2)))