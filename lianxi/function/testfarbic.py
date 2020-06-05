import os
import re

import fabric


# import  urlparse
# from urllib.parse import urlparse
def jar_deploy():
    current_path = os.getcwd()
    print(current_path)
    modulename = 'jiapengtest'
    find_str = 'Template'
    replace_str = str(modulename)
    f = open(f'{current_path}/template.sh', 'r', encoding='utf-8')
    f_new = open('start.sh', 'w', encoding='utf-8')
    for line in f:
        if find_str in line:
            line = line.replace(find_str, replace_str)
        f_new.write(line)
    f.close()
    f_new.close()
    command = f'fab -f {current_path}/fabricfile.py -H 192.168.1.186 jar_mkdir_service:module={modulename},source={current_path}/start.sh'
    os.system(command)


def testmatch():
    current_path = os.getcwd()
    f = open(f'{current_path}/deploydayu -jiatest.sh', 'r', encoding='utf-8')
    line = f.read()
    replaceline = re.search(r'dayu_module_list=(.+?))', line)
    print(replaceline.group())


# jar_deploy()
testmatch()
