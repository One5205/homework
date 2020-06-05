import json
import os


def testjson():
    current_path = os.path.abspath('.')
    print(current_path)
    with open(current_path + '\\test.json', 'r') as f:
        # filedata=f.read()
        # print(filedata)

        content = f.read()
        # filed = json.loads(content)
        file = current_path + '\\test.json'
        filed=json.load(f)
        print("filed:", content)
        print('--------------')
        print(filed)

testjson()
