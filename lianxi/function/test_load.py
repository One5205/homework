from functools import singledispatch


@singledispatch
def function(obj):
    print('%r' % (obj))


@function.register(int)
def function_int(obj):
    print('Integer: %d' % (obj))


@function.register(str)
def function_int(obj):
    print('String: %s' % (obj))


@function.register(list)
def function_list(obj):
    print('List: %r' % (obj))


if __name__ == "__main__":
    function(1)
    function('hello')
    function(range(3))
    function(object)
    function([1,2,3])
