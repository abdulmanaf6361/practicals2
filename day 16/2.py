class Father:
    def work(self):
        print("Im a farmer")

class Son(Father):
    pass

son = Son()
son.work()