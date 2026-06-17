class Person:
    def __init__(self,name,role):
        self.name = name
        self.role = role

groom = Person("Virat", "groom")
bride = Person("Anushka", "bride")
bride_father = Person("Ashok", "bride father")
groom_father = Person("Prem", "groom father")
uncle = Person("Ramesh", "uncle")
aunt = Person("Suresh", "aunt")

class Marriage:
    def __init__(self, bride, groom):
        self.bride = bride
        self.groom = groom
        self.__budget = 5000000

    def show_budget(self, role):
        allowed_people = ["bride", "groom", "bride father", "groom father"]
        if role in allowed_people:
            print("Budget is", self.__budget)
        else:
            print("You are not allowed to see the budget")

virushka_marriage = Marriage(bride, groom)
virushka_marriage.show_budget("uncle")
virushka_marriage.show_budget("groom father")