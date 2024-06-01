from abc import abstractmethod, ABC

# № 1) Реализуйте систему интернет магазинов.Каждый магазин реализован через абстракцию как и каждый товар каждого магазина.

class Product(ABC):
    def __init__(self, name, price, desc) -> None:
        self.name = name
        self.price = price
        self.desc = desc
    
    def __str__(self) -> str:
        return f"{self.name}, {self.price}, {self.desc} \n"
    
    
class Flower(Product):
    def __init__(self, name, price, desc, form) -> None:
        super().__init__(name, price, desc)
        self.form = form
        
class TV(Product):
    def __init__(self, name, price, desc, size) -> None:
        super().__init__(name, price, desc)
        self.size = size


class Shop(ABC):
    def __init__(self, name, address, link) -> None:
       self.name = name
       self.address = address
       self.link = link
       self.products = []
       
    def __str__(self) -> str:
        return  f"{self.name}, {self.address}, {self.link} \n"
    
    @abstractmethod
    def add_product(self, product):
        pass
        
    @abstractmethod
    def add_products(self, *args):
        pass
            
    @abstractmethod  
    def show_products(self):
        pass
    

class FruitShop(Shop):
    
    def add_product(self, product):
        self.products.append(product)

    def add_products(self, *args):
        for product in args:
            self.products.append(product)

    def show_products(self):
        for product in self.products:
            print(F"Product: {product}")
            
class ElectronicShop(Shop):
    
    def add_product(self, product):
        self.products.append(product)

    def add_products(self, *args):
        for product in args:
            self.products.append(product)

    def show_products(self):
        for product in self.products:
            print(F"Product: {product}")
    

class AreaShop():
    def __init__(self) -> None:
        self.shops = []
        
    def add_shop(self, shop):
        self.shops.append(shop)
        
    def print_shops(self):
        for shop in self.shops:
            print(shop)
            
            
flower1 = Flower("Carnations", 30, "desc", "Roza")
flower2 = Flower("Dahlias", 25, "desc", "Crocus")

electro1 = TV("Thosiba UD6653", 10100, "Ultra", "55")
electro2 = TV("Samsung LG HJ7755", 7500, "Oled", "48")
            
electric_shop = ElectronicShop("Bomba", "bd. Moscova 1", "www.bomba.md")
electric_shop.add_product(electro1)
electric_shop.add_product(electro2)
electric_shop.show_products()

flower_shop = ElectronicShop("Flower One", "bd. Dacia 11", "www.best-flower.md")
flower_shop.add_product(flower1)
flower_shop.add_product(flower2)
flower_shop.show_products()

area_shop = AreaShop()

area_shop.add_shop(electric_shop)
area_shop.add_shop(flower_shop)
area_shop.print_shops()


 
# № 2) Реализуйте остановки где могут остановливаться различные транпосртные средства.
# Каждый транспорт имеет минимум один уникальный метод и минимиум одно уникальное поле.
# Используйте минимум один интерфейс в прогрмме.Сохраните все транспорты в словарь где ключ вид транспорта,
# значенение перечелсния всех моделей и их номеров давнного вида : {"moto" : {"moto1" : "ABC123" ...}...}

class Transport(ABC):
    def __init__(self, name, year, vin, category ) -> None:
       self.name = name
       self.year = year
       self.vin = vin
       self.category = category
    
    @abstractmethod
    def move(self):
        pass
    

class Moto(Transport):
    def __init__(self, name, year, vin, category, has_sidecar) -> None:
        super().__init__(name, year, vin, category)
        self.has_sidecar = has_sidecar
    
    def move(self):
        print(f"{self.name} is moving on the road")
        
    def willi(self):
     print(f"{self.name} willie does")
     
     
class Cargo(Transport):
    def __init__(self, name, year, vin, category, capacity) -> None:
        super().__init__(name, year, vin, category)
        self.capacity = capacity

    def move(self):
        print(f"{self.name} is moving on the weather")

    def drop_anchor(self):
        print(f"{self.name} is dropped anchor")

moto1 = Moto("Street RRT", 2005, "A12312354411", "Moto", False)
moto2 = Moto("Gold 2000", 2050, "A64574576345f", "Moto", True)

cargo1 = Cargo("Poli BLU 10", 2000, "A234234234", "Cargo",  10000)
cargo2 = Cargo("Koko 22", 2000, "A456456456", "Cargo", 5000)

moto1.move()
moto1.willi()

cargo1.move()
cargo1.drop_anchor()

