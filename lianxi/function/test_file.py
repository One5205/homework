with open('wenjiantest', mode='r', encoding="utf-8") as wen:
    # wen.write('\nhello python11112')
    # wen.seek(1,0)
    # print(wen.read())
    # content=wen.read()
    # for i in content:
    #     print(i)
    for i in wen:
        print(i.strip())  # Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。

        # 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
    # for i in wen:
    #     print(i)

# mode='a+':在文件末尾追加写入内容，不清空

# mode=w或w+：会覆盖原来内容


#
# # list=[1,'5','jia','peng']
# # for i in list:
# #     print(i)
#
#
# f = "lucky.txt"
#
# a =8
# with open(f,"w") as file:   #”w"代表着每次运行都覆盖内容
#     for i in range(a):
#         file.write(str(i) + "d" + " "+"\n")
#     # a +=1
