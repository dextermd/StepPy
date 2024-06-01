from Todo import Task, ToDoList

def main():
    to_do = ToDoList()
    while True:
        print("1. Add Task")
        print("2. Mark task as done")
        print("3. Print Tasks")
        print("4. Print Completed Tasks")
        print("5. Print Uncompleted Tasks")
        print("6. Remove Task By Index")
        print("7. Find Task by Name")
        print("8. Edit Task Description by index")
        print("9. Exit")
        
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                name = input("Enter task name: ")
                description = input("Enter task description: ")
                to_do.add_task(name, description)
            case 2:
                index = int(input("Enter task index: "))
                to_do.mark_task_as_complete_by_index(index)
            case 3:
                to_do.print_tasks()
            case 4:
                to_do.print_completed_tasks()
            case 5:
                to_do.print_uncompleted_tasks()
            case 6:
                index = int(input("Enter task index: "))
                to_do.remove_task_by_index(index)
            case 7:
                name = input("Enter task name: ")
                found_tasks = to_do.find_task_by_name(name)
                if len(found_tasks) == 0:
                    print("Task not found")
                else:
                    for task in found_tasks:
                        print(task)
            case 8:
                index = int(input("Enter task index: "))
                new_task_description = input("Enter new task description: ")
                to_do.edit_task_description(index, new_task_description)
            case 9:
                print("Thank you for using my app")
                break
            case _:
                print("Invalid choice")
                continue

if __name__ == "__main__":
    main()
    
    
# Cоздайте магазин.Каждый товар представлен в виде словаря,в вашем магазине есть категории и фильтрации/поиски.
# Также у каждого товара есть его количество,при достижении 0 товар исчезает со склада.Пользователь умеет покупать товары