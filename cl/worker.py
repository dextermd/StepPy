from human import Human

class Worker(Human):
    def __init__(self, name, age, salary, spec) -> None:
        super().__init__(name, age)
        self.salary = salary
        self.spec = spec
                
    def __str__(self) -> str:
        return f"{super().__str__()}, {self.spec}, {self.salary}"