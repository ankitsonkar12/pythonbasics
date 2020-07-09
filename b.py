def foo(**kwargs):
    return max(kwargs, key = kwargs.get)
print(foo(a=1,b=5,c=3))    