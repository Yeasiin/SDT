def fun1(*arg):
    print(type(arg))


def fun2(**arg):
    print(type(arg))


print(fun1("hello", "Arfat","hello"))
print(fun2(name="hello"))