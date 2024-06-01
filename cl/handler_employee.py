class HandlerEmployee:
    def __init__(self, company):
        self.company = company

    def add_employee(self, employee):
        self.company.employees.append(employee)
        print(f"Add: {employee.name}")

    def delete_employee(self, employee):
        self.company.employees.remove(employee)
        print(f"Remove: {employee.name}")