a = 10
print(id(a))
b = 20
print(id(b))

def add(a, b):
    print("inside function")
    print(id(a))
    print(id(b))
    return a + b

result = add(a, b)
print("after function call")
print(id(a))
print(id(b))
print(result)