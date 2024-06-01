from book import Book
from library import Library
from user import User

class Car:
    wheels =4
    
    # метод который отвечает за создание обьекта в python
    def __init__(self, make, model, year, color) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        

    
    # Магические методы - специальные методы созданные разработчиками языка, которые имеют каждый некий специальный функционал
    # Вызываются автоматически при  определенных условиях
    # __str__ - магический метод который вызывается при показе обьекта через функцию print(), возвращает сроку и работает поп ринципу 
    # toString(), когда информация об обьекте выводится при обращении напрям ую к обьекту
    def __str__(self) -> str:
        return f"\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}\nColor: {self.color}"
    
    def drive_car(self) -> None:
        print(f"{self.color} {self.model} its on the way")
        
    @staticmethod
    def set_price_for_fabric(price):
        return price
    
        
        
car1 = Car("Nissan", "GTR-34", 1998, "Blue")
car2 = Car("Toyota", "Prius", 2021, "White")
car3 = Car("Honda", "Accord", 2019, "Black")

print(car1)
print(car2)
print(car3)



car1.drive_car()

value = car1.set_price_for_fabric(200)

print(value)

book1 = Book("Harry Potter and the goblet of fire", "J.K. Rowling")
book2 = Book("Golden Compass", "Philip Pullman")

print("--------------------------Each Book-----------------------------")
print(book1)
print(book2)

print("--------------------------Library-----------------------------")
lib1 = Library()
lib1.add_book(book1)
lib1.add_book(book2)
lib1.show_library()
lib1.show_users()

print("--------------------------User-----------------------------")
user1 = User("Vasia", 20, "068006644")
user2 = User("Misha", 26, "068009911")
lib1.add_user(user1) 
lib1.add_user(user2)
lib1.show_users()
lib1.reserv_book(user1, book1);
lib1.show_library()
lib1.reserv_book(user1, book1);
lib1.delete_book(book2)
lib1.show_library()

# Добавьте класс пользователь который может зарегестрироваться в библоиотеке и брать книги.Если взятую уже книгу 
# попытается взять кто то другой мы собщаем что книга уже занята,после возрата ее можно будет вновь брать.Добавьте
# возможность удалить книгу из библиотеки.