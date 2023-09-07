def sum(*args):
    result = 0
    for arg in args:
        if isinstance(arg, list):
            result += sum(*arg)
        else:
            result += arg
    return result

# v = sum(1,3,4,5,6)
# print(v)