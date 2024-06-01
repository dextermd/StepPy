class Human:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f"Name: {self.name}, {self.age}"
