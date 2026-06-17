l = [1,2,3]
print(id(l))

def fn(l):
    print("inside function")
    print("before",id(l))
    l.append(4)
    print("after",id(l))

fn(l)
print("outside")
print(id(l))