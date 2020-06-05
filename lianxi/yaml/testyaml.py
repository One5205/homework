import json
import os

import yaml


def get_yaml_data(yaml_file):
    # 打开yaml
    print('获取yaml数据')
    file = open(yaml_file, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()

    print(file_data)
    print("类型:", type(file_data))

    # 将字符串转化为字典或列表
    print('*****转化yaml数据为字典或列表*****')
    # data = yaml.load(file_data,Loader=yaml.FullLoader)
    data = yaml.load(file_data)
    print(data)
    print("类型", type(data))
    return data

    data1=yaml.load(file,Loader=yaml.SafeLoader)
    print('---------------',data1)


current_path = os.path.abspath(".")
yamlfile = os.path.join(current_path, "myyaml.yaml")
get_yaml_data(yamlfile)

