class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        self.__balance = balance

ramesh = Account("Ramesh", 5000)
suresh = Account("Suresh", 10000)
print(ramesh.get_balance())
print(suresh.get_balance())
ramesh.set_balance(2000)
print(ramesh.get_balance())