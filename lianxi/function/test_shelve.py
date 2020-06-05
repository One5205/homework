import shelve
s = shelve.open('test_shelve.db')

def test_shelve1():
    try:
        s['kk']={'int':10,'float':9.5,'string':'sample data'}
        s['MM']=[1,2,3]
        print(s['kk'])
        print('hello world')
    finally:
        s.close()

test_shelve1()



def test_shelve2():
    try:
        s = shelve.open('test_shelve.db')
        value=s['kk']
        print(value)
    finally:
        s.close()

test_shelve2()

def test_shelve3():
    try:
        s=shelve.open('test_shelve.db')
        # del s['kk']
        #修改
        s['kk']={'striing':'day day up'}
        value=s['kk']
        print(value)
    finally:
        s.close()

test_shelve3()