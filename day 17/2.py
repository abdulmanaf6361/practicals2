# def fun(x=[]):
#     x.append(1)
#     return x
# print(fun(),fun())

# print(type(lambda x: x))

# a = [1, 2, 3]
# print(a[-1])

# print(10/3)

# print({1,2,3} & {2,3,4})

def den():
    yield 1
    yield 2

g = den()
print(next(g))
print(next(g))