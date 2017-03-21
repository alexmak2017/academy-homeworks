class Animal:

    def __init__(self,food_per_day,period):
        self.food_per_day = food_per_day
        self.period = period

    def food_for_period(self):
        return float(self.food_per_day.split()[0])*int(self.period.split()[0])

class Carnivores(Animal):
    def eat_meat(self):
        food_c = "This animal eat meat"
        return food_c

class Omnivores(Animal):
    def eat_meat(self):
        food_o = "This animal eat meat"
        return food_o

    def eat_plant(self):
        food_o = "This animal eat plant"
        return food_o

class Herbivore(Animal):
    def eat_plant(self):
        food_h = "This animal eat plant"
        return food_h


def animal_check(name):
    try:
        print(name.eat_plant())
    except AttributeError:
        print("This animal don't eat plant")

wolf = Carnivores("2.5 kg", "12 days")
animal_check(wolf)
print(wolf.food_for_period(),"kg")

cow = Omnivores("5.1 kg", "18 days")
animal_check(cow)
print(cow.food_for_period(),"kg")

pig = Herbivore("3 kg","23 days")
animal_check(pig)
print(pig.food_for_period(),"kg")

