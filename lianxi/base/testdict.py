import requests


def get_membercardcode_list():
    '''
    :return:返回会员memberCardCode的list
    '''
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJBcHBDb2RlIjoiZGVmYXVsdCIsIlRlbmFudElkIjoyNTgsIlVzZXJOYW1lIjoiY3N5eXp4MDIiLCJV' \
            'c2VySWQiOjUyMiwiQnJhbmNoSWQiOjg4OTQsImV4cCI6MTU5Mjg5MTk0NiwiQXBwTmFtZSI6ImRlZmF1bHQifQ.5fPwRRqW2n3fxFbnXTOvRmAtrVksHqchBGgfTyzRkoE'
    headersdayu = {"Content-Type": "application/json;charset=UTF-8", "token": token}
    base_domain = 'http://fe1.rongyi.com:8186'
    url = base_domain + '/buorg/v1/member?size=2&current=1'
    r = requests.get(url, headers=headersdayu)
    rb = r.text
    print(rb)
    memberlist = []  # 定义一个空列表，用于存储会员cardcode
    # for i in rb:
    #     print('---------------------')
    #     print(i)
    #     # memberlist.append(i)
    # print(memberlist)

    # print('随机会员cardcode:', random.choice(membercardcodelist))
    #
    # return membercardcodelist  # 返回会员cardcode

    # print(r.json()['data']['records'])


get_membercardcode_list()
