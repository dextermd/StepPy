class User:
    def __init__(self, name, age, phone) -> None:
        self.name = name
        self.age = age
        self.phone = phone
        
    def __str__(self) -> str:
        return f"Name: {self.name}, Phone: {self.phone}"