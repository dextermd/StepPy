# class A:
#     a_field = "field from A"
#     def printA(self):
#         print("method from A")
        
# class B(A):
#     pass

# a = A()
# b = B()

# a.printA()
# b.printA()


class Zoo:
    def __init__(self):
        self.animals = []
        
    def add_animal(self, animal):
        self.animals.append(animal)
        
    def print_animals(self):
        for animal in self.animals:
            print(animal)


class Carnivore:
    def eat(self):
        print(f"{self.species} is eating meat")
        
class Herbivore:
    def eat(self):
        print(f"{self.species} is eating herbivore food")

class GeneralCharacteristichAnimal:
    def __init__(self, name, age, species) -> None:
        self.name = name
        self.age = age
        self.species = species
        
class Horses(Herbivore, GeneralCharacteristichAnimal):
    def __init__(self, name, age, species, speed) -> None:
        super().__init__(name, age, species)
        self.speed = speed
        
    def gallop(self):
        print(f"{self.name} is running with {self.speed} km/h")
    
class Birds(Carnivore, GeneralCharacteristichAnimal):
    has_feathers = True
    def fly(self):
        print(f"{self.name}This animal is flying")

zebra = Horses("Martin", 4, "African Zebra", 60)
zebra.gallop()
zebra.eat()

print("---------------------------------------------------------")

swan = Birds("Utionok", 1.5, "Common Swan")
swan.eat()
swan.fly()


# Создайте класс работник с полями на выбор.Создвйте Менеджера который имеет список людей в подчинений и департамент
# к которому он относится.Создайте программиста который работает на определенном Я.П. Создайте тим лида который управляет
# программистами.Создайте Босса который умеет нанимать увольняет людей из своей компании через специальный класс ХэндлерСотрудников