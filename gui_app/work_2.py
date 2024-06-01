import sqlite3
import flet as ft

db_name = "students.db"

def init_db():
    conn = sqlite3.connect(db_name)         # Создает соединение с базой данных
    cursor = conn.cursor()                  # Создает объект курсора
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grades TEXT,
        scool TEXT NOT NULL
    )
    ''')                                    # Создает таблицу "table_name", если она не существует
    conn.commit()                           # Исполняет SQL-запрос и сохраняет изменения в базе данных
    conn.close()                            # Закрывает соединение с базой данных
    
# CRUD

def create(name, age, scool, grades=None):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    grades_str = ','.join(map(str, grades)) if grades else None
    cursor.execute("INSERT INTO students (name, age, grades, scool) VALUES (?, ?, ?, ?)", (name, age, grades_str, scool))
    conn.commit()
    conn.close()
    
    
def get_all():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    conn.close()
    return data

def get_by_id(id):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (id,))
    data = cursor.fetchone()
    conn.close()
    return data

def find_by_id(id):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (id,))
    data = cursor.fetchone()
    conn.close()
    return data

def update(id, name, age, scool, grades=None):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    grades_str = ','.join(map(str, grades)) if grades else None
    cursor.execute("UPDATE students SET name = ?, age = ?, grades = ?, scool = ? WHERE id = ?", (name, age, grades_str, scool, id))
    conn.commit()
    conn.close()
    
def delete(id):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    
init_db()


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "Список студентов"
    
    def grades_average(grades):
        if grades:
            numeric_grades = list(map(int, grades))
            return sum(numeric_grades) / len(numeric_grades)
        return 0
        
    
    def get_grades_array(grades_container):
        grades = []
        for grade_input in grades_container:
            if isinstance(grade_input, ft.TextField) and grade_input.value:
                grades.append(int(grade_input.value))
        return grades
    
    def get_grades_array_by_str(grades_str):
        grades = []
        grades = grades_str.split(',') if grades_str else []
        return grades
    
    def load_students():
        students = get_all()
        student_list.controls.clear()
        for student in students:
            grades = get_grades_array_by_str(student[3])
            print(grades_average(grades))
            text_style = ft.TextStyle(size=20, color=ft.colors.RED) if grades_average(grades) < 5 else ft.TextStyle(size=20, color=ft.colors.GREEN)
            student_list.controls.append(
                ft.Row(
                    [
                        ft.Text(student[1] , style=text_style),
                        ft.Text(student[2] , style=text_style),
                        ft.Text(student[3] , style=text_style),
                        ft.Text(student[4], style=text_style),
                        ft.IconButton( icon="edit", on_click=lambda event, std=student: edit_student(std)),
                        ft.IconButton( icon="delete", on_click=lambda event, std=student: delete_student_ui(std)),
                    ],
                )
            )
        page.update()

    name_input = ft.TextField(
        width=450,
        label="Имя",
        hint_text="Введите имя",
        border_color=ft.colors.BLUE_600,
        text_style=ft.TextStyle(size=14, color=ft.colors.BLACK87)
    )
    
    age_input = ft.TextField(
        width=450,
        label="Возраст",
        hint_text="Введите возраст",
        border_color=ft.colors.BLUE_600,
        text_style=ft.TextStyle(size=14, color=ft.colors.BLACK87)
    )
    
    school_input = ft.TextField(
        width=450,
        label="Школа",
        hint_text="Введите школу",
        border_color=ft.colors.BLUE_600,
        text_style=ft.TextStyle(size=14, color=ft.colors.BLACK87)
    )
    
    student_list = ft.Column()
    
    grades_container = ft.Row()
    
    def add_grade_input(event):
        new_grade_input = ft.TextField(
            width=80,
            label="Оценка",
            label_style=ft.TextStyle(size=12, color=ft.colors.BLACK87),
            hint_text="Введите оценку",
            border_color=ft.colors.BLUE_600,
            text_style=ft.TextStyle(size=12, color=ft.colors.BLACK87)
        )
        grades_container.controls.append(new_grade_input)
        page.update()
    
    add_grade_button = ft.IconButton(
            icon=ft.icons.ADD,
            on_click= lambda event: add_grade_input(event)
        )
    
    add_btn = ft.ElevatedButton(
        bgcolor=ft.colors.BLACK,
        color=ft.colors.WHITE,
        text="Добавить",
        on_click=lambda event: create_student_ui(event),
    )
    
    add_btn = ft.ElevatedButton(
        bgcolor=ft.colors.BLACK,
        color=ft.colors.WHITE,
        text="Добавить",
        on_click=lambda event: create_student_ui(event),
    )
        
    input_container = ft.Container(
        content = ft.Column(
            [
                name_input,
                age_input,
                ft.Row(controls=[grades_container, add_grade_button]),
                school_input,
                add_btn
            ],
            spacing=20
        ),
        padding=20,
    )
    
    page.add(
        input_container,
        ft.Divider(),
        ft.ListView(controls=[student_list])
    )
     
    load_students()
    
    def create_student_ui(event):
        grades = get_grades_array(grades_container.controls)
        create(name_input.value, age_input.value, school_input.value, grades)
        
        name_input.value = ""
        age_input.value = ""
        school_input.value = ""
        grades_container.controls.clear()
        load_students()
        
    def edit_student(std):
        name_input.value = std[1]
        age_input.value = str(std[2])
        school_input.value = std[4]
        
        grades = std[3].split(',') if std[3] else []
        grades_container.controls.clear()
        for grade in grades:
            grade_input = ft.TextField(
                width=80,
                label="Оценка",
                hint_text="Введите оценку",
                value=grade,
                border_color=ft.colors.BLUE_600,
                text_style=ft.TextStyle(size=14, color=ft.colors.BLACK87)
            )
            grades_container.controls.append(grade_input)
        
        add_btn.text = "Обновить"
        add_btn.on_click = lambda event: update_student_ui(std[0])
        page.update()
            
    def update_student_ui(student_id):
        grades = []
        for grade_input in grades_container.controls:
            if isinstance(grade_input, ft.TextField) and grade_input.value:
                grades.append(int(grade_input.value))
        update(student_id, name_input.value, age_input.value, school_input.value, grades)
        name_input.value = ""
        age_input.value = ""
        school_input.value = ""
        grades_container.controls.clear()
        add_btn.text = "Добавить"
        add_btn.on_click = create_student_ui
        load_students()
        
    def delete_student_ui(std):
        delete(std[0])
        load_students()
        
    add_grade_input(None)
    
ft.app(target=main)