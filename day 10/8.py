a = 10
print("first id",id(a))

def fn(a):
    print("inside function")
    print("before",id(a))
    a = a + 10
    print("after",id(a))
    return a

ans = fn(a)
print(id(a))
print(id(ans))