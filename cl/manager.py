from human import Human

class Manager(Human):
    def __init__(self, name, age, team_members, departament) -> None:
        super().__init__(name, age)
        self.team_members = team_members
        self.departament = departament
        
    def add_team_member(self, worker):
        self.team_members.append(worker) 
    
    def __str__(self):
        team_str = ', '.join([worker.name for worker in self.team_members])
        return f"{super().__str__()}, Department: {self.department}, Team Members: {team_str}"