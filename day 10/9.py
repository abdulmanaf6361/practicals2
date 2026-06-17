a = 10

def fn(a):
    print("inside function")
    print("before",id(a))
    a = a + 10
    print("after",id(a))
    
fn(a)
print("outside")
print(id(a))