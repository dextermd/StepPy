from abc import abstractmethod, ABC

# абстракция  - ООП методологияя которая позволяет создать маштабируемые приложени
# благолоря интерфэйсам и абстрактным классам

# абстрактный класс - класс который имеет минимум один абстрактный метод. 
# Данный классы лишены возможности создавать обьекты 

# абстрактный метод - метод который не имеет реализацию и создается с помощью декоратора @abstractmethod

# интерфейсы - абстр. клвссы которые имеют только абстрактные методы

# class A(ABC):
    
#     def method_a(self):
#         pass
    
#     @abstractmethod
#     def method_b(self):
#         pass
    

# class IShape(ABC):
#     @abstractmethod
#     def area(self):
#         pass


# class Rect(IShape):
#     def __init__(self, a, b) -> None:
#         self.a = a
#         self.b = b
        
#     def area(self):
#         return self.a * self.b
    
# rext = Rect(10, 20)


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

class Dino(ABC):
    def __init__(self, name, breed, weight, height, diet) -> None:
        self.name = name
        self.breed = breed
        self.weight = weight
        self.height = height
        self.diet = diet
        
    def __str__(self) -> str:
        return  f"{self.breed} ({self.name} : {self.weight}kg, {self.height}m, Diet: {self.diet})\n"
    
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def sleep(self):
        pass
    
class SwimingDino(Dino):
    def __init__(self, name, breed, weight, height, diet) -> None:
        super().__init__(name, breed, weight, height, diet)
    
    def move(self):
        print(f"{self.name} is flying")

    def eat(self):
        print(f"{self.name} is eat {self.diet}")

    def sleep(self):
        print(f"{self.name} is sleeping on a tree")
        
class FlyingDino(Dino):
    def __init__(self, name, breed, weight, height, diet) -> None:
        super().__init__(name, breed, weight, height, diet)
    
    def move(self):
        print(f"{self.name} is flying")

    def eat(self):
        print(f"{self.name} is eating {self.diet}")

    def sleep(self):
        print(f"{self.name} is sleeping in a tree")

class GroundDino(Dino):
    def __init__(self, name, breed, weight, height, diet) -> None:
        super().__init__(name, breed, weight, height, diet)
        
    def move(self):
        print(f"{self.name} is running")

    def eat(self):
        print(f"{self.name} is eating {self.diet}")

    def sleep(self):
        print(f"{self.name} is sleeping in den")
    
class DinoPark:
    def __init__(self) -> None:
        self.dinos = []
        
    def add_dino(self, *args):
        for dino in args:
            self.dinos.append(dino)
        
    def print_dinos(self):
        for dino in self.dinos:
            print(dino)
            

jurassic_park = DinoPark()

dino1 = GroundDino("Velik", "Velociraptor", 15, 0.5, "meat")
dino2 = FlyingDino("Qetz", "Quetzalcoatlus", 220, 12, "fish and meat")
dino3 = SwimingDino("Mossy", "Mosasaurus", 10000, 17, "fish and meat")

jurassic_park.add_dino(dino1, dino2, dino3)

jurassic_park.print_dinos()