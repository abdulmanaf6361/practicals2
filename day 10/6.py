a = 10
print(id(a))
b = 20
print(id(b))

def add(c, d):
    print("inside function")
    print(id(c))
    print(id(d))
    return c+d

result = add(a, b)
print("after function call")
print(id(a))
print(id(b))
print(result)