class Task:
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
        self.completed = False
        
    def __str__(self) -> str:
        completed_str = "Complited" if self.completed == True else "Pending"
        return f"{self.name} = {self.description} ({completed_str})"
    
    def mark_as_complete(self):
        self.completed = True

class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, name, description):
        self.tasks.append(Task(name, description))
    
    def mark_task_as_compleate_by_index(self, index):
        index -= 1
        if index < 0 or index >= len(self.tasks):
            print("Task index out of range")
            return None
        
        self.tasks[index].mark_as_complete()
        print(f"{index + 1} Task completed!")
        
    def print_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")
                
    def print_completed_tasks(self):
        for index, task in enumerate(self.tasks):
            if task.completed:
                print(f"{index + 1}. {task}")

    def print_uncompleted_tasks(self):
        for index, task in enumerate(self.tasks):
            if not task.completed:
                print(f"{index + 1}. {task}")
    
    def remove_task_by_index(self, index):
        index -= 1
        if index < 0 or index >= len(self.tasks):
            print("Task index out of range")
            return None
        
        del self.tasks[index]
        print(f"{index +1 } Task removed!")
        
    def find_task_by_name(self, name):
        found_tasks = [ task for task in self.tasks if task.name == name] #comprehension
        return found_tasks
    
    def edit_task_description(self, index, new_descr):
        index -= 1
        if index < 0 or index >= len(self.tasks):
            print("Task index out of range")
            return None
        
        self.tasks[index].description = new_descr
        print(f"{index + 1 } Task dexcription changed!")