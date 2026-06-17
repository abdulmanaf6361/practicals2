class Father:
    def work(self):
        print("Im a farmer")

class Son(Father):
    def work(self):
        super().work()
        print("Im engineer")
    

son = Son()
son.work()
