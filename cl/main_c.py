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
    def __init__(self, meat_type) -> None:
        self.meat_type = meat_type
        
    def eat(self):
        print(f"{self.species} is eating {self.meat_type}")
 
 
class Herbivore:
    def __init__(self,is_big_animal) -> None:
        self.is_big_animal = is_big_animal
    def eat(self):
        print(f"{self.species} is eating herbivore food")
 
 
class GeneralCharacteristichAnimal:
    def __init__(self, name,age,species) -> None:
        self.name = name
        self.age = age
        self.species = species
        
    def __str__(self) -> str:
        return f"{self.name}, {self.species}"
 
 
# Класс Миксин - Когда у класса два и больше предка
# super().method() - функция которая вызввает метод из первого переданного родителя дабы имеласб возможность дополнить фунционал
# в предке без того что бы изменять метод родителя
"""
В случае если вам нужен один и тот же метод который требутеся дополнить и скопировать из 2х и больше классов,не используем
super() так как он берет только от первого родителя.Мы напрямую вызываем от каждого класса его метод там где хотим дополнить
"""
class Horses(Herbivore, GeneralCharacteristichAnimal):
    def __init__(self,is_animal_big,name,age,species,speed):
        # super().__init__(name,age,species)
        Herbivore.__init__(self,is_animal_big)
        GeneralCharacteristichAnimal.__init__(self,name,age,species)
        self.speed = speed
    def gallopp(self):
        print(f"{self.name} is running with {self.speed} km/h")

 
class Birds(Carnivore,GeneralCharacteristichAnimal):
    def __init__(self,meat_type,name,age,species,has_feathers):
        Carnivore.__init__(self, meat_type)
        GeneralCharacteristichAnimal.__init__(self,name,age,species)
        self.has_feathers = has_feathers
    
    def fly(self):
        print(f"{self.name} animal is flying")
 
zebra = Horses(True,"Martin",4,"African Zebra",60)
 
swan = Birds("fish", "Utionak",1.5, "Common Swan", False)

print(zebra)
print(swan)

print("---------------------------------------------------")
 
zebra.gallopp()
zebra.eat()

print("---------------------------------------------------")

swan.eat()
swan.fly()