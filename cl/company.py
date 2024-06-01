from typing import List
from worker import Worker

class Company:
    def __init__(self, company_name, created_year) -> None:
        self.company_name = company_name
        self.created_year = created_year
        self.employees: List[Worker] = []
    
    def __str__(self) -> str:
        return f"Company name: {self.company_name}, created {self.created_year}"
    
    def hire_employee(self, employee : Worker):
        self.employees.append(employee)
        print(f"{employee.name}")