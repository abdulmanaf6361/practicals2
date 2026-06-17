class Father:
    def __init__(self, land, house):
        self.land = land
        self.house = house

class Groom(Father):
    def __init__(self, land, house, salary):
        super().__init__(land, house)
        self.salary = salary

virat = Groom("10 acres", "2 bhk", 500000)

print(virat.land)
print(virat.salary)
virat.land = "20 acres"
print(virat.land)
print(virat.super().land)