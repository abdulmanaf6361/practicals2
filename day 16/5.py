class A:
    def work(self):
        print("im farmer")

class B(A):
    def work(self):
        print("im engineer")

class C(B):
    def work(self):
        print("im doctor")
    
class D(C):
    pass

class E(D):
    pass

obj = E()
obj.work()
obj1 = C()
obj1.work()