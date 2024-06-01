from human import Human
from company import Company

class Boss(Human, Company):
    def __init__(self, name, age, company_name, created_year, feature):
        Human.__init__(self, name, age)
        Company.__init__(self, company_name, created_year)
        self.feature = feature 
        
    def __str__(self) -> str:
        return f"{super().__str__()}, {self.feature}"

    def add(self, employee):
        self.employee_handler.add_employee(employee)

    def remove(self, employee):
        self.employee_handler.remove_employee(employee)