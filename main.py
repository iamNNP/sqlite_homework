import sqlite3

# Создание или подключение к базе данных SQLite
db_connection = sqlite3.connect('university.db')
cursor = db_connection.cursor()

def create_db():
    # Шаг 1: Создание таблицы
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        department TEXT NOT NULL, 
        date_of_birth DATETIME
    )
    """
    cursor.execute(create_table_query)
    print("Таблица 'Students' успешно создана.")

    create_table_query = """
    CREATE TABLE IF NOT EXISTS Teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        department TEXT NOT NULL
    )
    """
    cursor.execute(create_table_query)
    print("Таблица 'Teachers' успешно создана.")

    create_table_query = """
    CREATE TABLE IF NOT EXISTS Courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        teacher_id INTEGER, 
        FOREIGN KEY(teacher_id) REFERENCES Teachers(id)
    )
    """
    cursor.execute(create_table_query)
    print("Таблица 'Courses' успешно создана.")

    create_table_query = """
    CREATE TABLE IF NOT EXISTS Exams (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATETIME,
        course_id INTEGER,
        max_score INTEGER, 
        FOREIGN KEY(course_id) REFERENCES Courses(id)
    )
    """
    cursor.execute(create_table_query)
    print("Таблица 'Exams' успешно создана.")

    create_table_query = """
    CREATE TABLE IF NOT EXISTS Grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        exam_id INTEGER,
        score INTEGER, 
        FOREIGN KEY(student_id) REFERENCES Students(id), 
        FOREIGN KEY(exam_id) REFERENCES Exams(id)
    )
    """
    cursor.execute(create_table_query)
    print("Таблица 'Grades' успешно создана.")

def add_student(name, surname, department, date_of_birth):
    insert_query = "INSERT INTO Students (name, surname, department, date_of_birth) VALUES (?, ?, ?, ?)"
    student_to_insert = name, surname, department, date_of_birth
    cursor.execute(insert_query, student_to_insert)
    db_connection.commit()
    print("Запись успешно добавлена в таблицу 'Students'.")

def add_teacher(name, surname, department):
    insert_query = "INSERT INTO Teachers (name, surname, department) VALUES (?, ?, ?)"
    teacher_to_insert = name, surname, department
    cursor.execute(insert_query, teacher_to_insert)
    db_connection.commit()
    print("Запись успешно добавлена в таблицу 'Teachers'.")

def add_course(title, description, teacher_id):
    insert_query = "INSERT INTO Courses (title, description, teacher_id) VALUES (?, ?, ?)"
    course_to_insert = title, description, teacher_id
    cursor.execute(insert_query, course_to_insert)
    db_connection.commit()
    print("Запись успешно добавлена в таблицу 'Courses'.")

def add_exam(date, course_id, max_score):
    insert_query = "INSERT INTO Exams (date, course_id, max_score) VALUES (?, ?, ?)"
    exam_to_insert = date, course_id, max_score
    cursor.execute(insert_query, exam_to_insert)
    db_connection.commit()
    print("Запись успешно добавлена в таблицу 'Exams'.")

def add_grade(student_id, exam_id, score):
    insert_query = "INSERT INTO Grades (student_id, exam_id, score) VALUES (?, ?, ?)"
    grade_to_insert = student_id, exam_id, score
    cursor.execute(insert_query, grade_to_insert)
    db_connection.commit()
    print("Запись успешно добавлена в таблицу 'Grades'.")

def update_student(update_by, update_param, update_by_value, update_param_value):
    update_query = f"UPDATE Students SET {update_param} = ? WHERE {update_by} = ?"
    data_to_update = (update_param_value, update_by_value)
    cursor.execute(update_query, data_to_update)
    db_connection.commit()
    print(f"Таблица 'Students' успешно обновлена.")

def update_teacher(update_by, update_param, update_by_value, update_param_value):
    update_query = f"UPDATE Teacher SET {update_param} = ? WHERE {update_by} = ?"
    data_to_update = (update_param_value, update_by_value)
    cursor.execute(update_query, data_to_update)
    db_connection.commit()
    print(f"Таблица 'Teachers' успешно обновлена.")
    
def update_course(update_by, update_param, update_by_value, update_param_value):
    update_query = f"UPDATE Courses SET {update_param} = ? WHERE {update_by} = ?"
    data_to_update = (update_param_value, update_by_value)
    cursor.execute(update_query, data_to_update)
    db_connection.commit()
    print(f"Таблица 'Courses' успешно обновлена.")

def delete_student(delete_by, delete_by_value):
    delete_query = f"DELETE FROM Students WHERE {delete_by} = ?"
    user_to_delete = (delete_by_value,)
    cursor.execute(delete_query, user_to_delete)
    db_connection.commit()
    print(f"Пользователь '{delete_by_value}' успешно удален.")

def delete_teacher(delete_by, delete_by_value):
    delete_query = f"DELETE FROM Teachers WHERE {delete_by} = ?"
    user_to_delete = (delete_by_value,)
    cursor.execute(delete_query, user_to_delete)
    db_connection.commit()
    print(f"Пользователь '{delete_by_value}' успешно удален.")
    
def delete_course(delete_by, delete_by_value):
    delete_query = f"DELETE FROM Courses WHERE {delete_by} = ?"
    user_to_delete = (delete_by_value,)
    cursor.execute(delete_query, user_to_delete)
    db_connection.commit()
    print(f"Пользователь '{delete_by_value}' успешно удален.")

def delete_exam(delete_by, delete_by_value):
    delete_query = f"DELETE FROM Exams WHERE {delete_by} = ?"
    user_to_delete = (delete_by_value,)
    cursor.execute(delete_query, user_to_delete)
    db_connection.commit()
    print(f"Пользователь '{delete_by_value}' успешно удален.")

def get_students_by_department(department):
    select_query = "SELECT * FROM Students WHERE department = ?"
    cursor.execute(select_query, (department,))
    result = cursor.fetchall()
    print("\nДанные в таблице 'Students':")
    for row in result:
        print(f"ID: {row[0]}, Имя: {row[1]}, Фамилия: {row[2]}, Факультет: {row[3]}, Дата рождения: {row[4]}")

def get_courses_by_teacher(select_by, select_by_value):
    select_query = f"SELECT * FROM Courses JOIN Teachers ON (Courses.teacher_id = Teachers.id) WHERE {select_by} = ?"
    cursor.execute(select_query, (select_by_value,))
    result = cursor.fetchall()
    print("\nДанные в таблице 'Courses':")
    for row in result:
        print(*row)

def get_students_by_course(select_by, select_by_value):
    select_query = f"SELECT * FROM Courses JOIN Teachers ON (Teachers.id = Courses.teacher_id) JOIN Students ON (Students.department = Teachers.department) WHERE Courses.{select_by} = ?"
    cursor.execute(select_query, (select_by_value,))
    result = cursor.fetchall()
    for row in result:
        print(*row)

def get_students_marks_by_course(select_by, select_by_value):
    select_query = f"SELECT * FROM Courses JOIN Teachers ON (Teachers.id = Courses.teacher_id) JOIN Students ON (Students.department = Teachers.department) JOIN Grades ON (Grades.student_id = Students.id) WHERE Courses.{select_by} = ?"
    cursor.execute(select_query, (select_by_value,))
    result = cursor.fetchall()
    for row in result:
        print(*row[-8:])

def get_students_avg_mark_by_course(select_by, select_by_value):
    select_query = f"SELECT AVG(score) FROM Courses JOIN Teachers ON (Teachers.id = Courses.teacher_id) JOIN Students ON (Students.department = Teachers.department) JOIN Grades ON (Grades.student_id = Students.id) WHERE Courses.{select_by} = ?"
    cursor.execute(select_query, (select_by_value,))
    print(*cursor.fetchall()[0])

def get_student_avg_mark(select_by, select_by_value):
    select_query = f"SELECT * FROM Students JOIN Grades ON (Students.id = Grades.student_id) WHERE {select_by} = ?"
    cursor.execute(select_query, (select_by_value,))
    result = cursor.fetchall()
    for row in result:
        print(*row)

def get_students_avg_mark_by_department(select_by_value):
    select_query = f"SELECT AVG(score) FROM Students JOIN Grades ON (Students.id = Grades.student_id) WHERE department = ?"
    cursor.execute(select_query, (select_by_value,))
    print(*cursor.fetchall()[0])



# # Шаг 2: Вставка данных
# insert_query = "INSERT INTO Users (name, age) VALUES (?, ?)"
# users_to_insert = [
#     ("John Doe", 28),
#     ("Jane Smith", 32),
#     ("Alice Johnson", 24)
# ]
# cursor.executemany(insert_query, users_to_insert)
# db_connection.commit()
# print(f"{len(users_to_insert)} записей успешно добавлены в таблицу 'Users'.")

# # Шаг 3: Выборка данных
# select_query = "SELECT * FROM Users"
# cursor.execute(select_query)
# result = cursor.fetchall()
# print("\nДанные в таблице 'Users':")
# for row in result:
#     print(f"ID: {row[0]}, Имя: {row[1]}, Возраст: {row[2]}")

# # Шаг 4: Обновление данных
# update_query = "UPDATE Users SET age = ? WHERE name = ?"
# data_to_update = (29, "John Doe")
# cursor.execute(update_query, data_to_update)
# db_connection.commit()
# print(f"Возраст пользователя 'John Doe' успешно обновлен.")

# # Шаг 5: Выборка данных после обновления
# cursor.execute(select_query)
# result = cursor.fetchall()
# print("\nДанные в таблице 'Users' после обновления:")
# for row in result:
#     print(f"ID: {row[0]}, Имя: {row[1]}, Возраст: {row[2]}")

# # Шаг 6: Удаление данных
# delete_query = "DELETE FROM Users WHERE name = ?"
# user_to_delete = ("Alice Johnson",)
# cursor.execute(delete_query, user_to_delete)
# db_connection.commit()
# print(f"Пользователь 'Alice Johnson' успешно удален.")

# # Шаг 7: Окончательная выборка данных после удаления
# cursor.execute(select_query)
# result = cursor.fetchall()
# print("\nДанные в таблице 'Users' после удаления:")
# for row in result:
#     print(f"ID: {row[0]}, Имя: {row[1]}, Возраст: {row[2]}")

# Закрытие соединения

print("Выберите команду: ")
print("""1. Добавление нового студента.
2. Добавление нового преподавателя.
3. Добавление нового курса.
4. Добавление нового экзамена.
5. Добавление нового оценки.
6. Изменение информации о студентах.
7. Изменение информации о преподавателях.
8. Изменение информации о курсах.
9. Удаление студентов.
10. Удаление преподавателей.
11. Удаление курсов.
12. Удаление экзаменов.
13. Получение списка студентов по факультету.
14. Получение списка курсов, читаемых определенным преподавателем.
15. Получение списка студентов, зачисленных на конкретный курс.
16. Получение оценок студентов по определенному курсу.
17. Средний балл студента по определенному курсу.
18. Средний балл студента в целом.
19. Средний балл по факультету.
20. Выйти из программы.
""")
create_db()
user_input = int(input())
while user_input != 20:
    create_db()
    if user_input == 1:
        print("Введите имя студента: ")
        name = input()
        print("Введите фамилию студента: ")
        surname = input()
        print("Введите факультет студента: ")
        department = input()
        print("Введите дату рождения студента: ")
        date_of_birth = input()
        try:
            add_student(name, surname, department, date_of_birth)
        except Exception as e:
            print(e)
            print("Ошибка при вводе команд, введите данные снова")
    if user_input == 2:
        print("Введите имя преподавателя: ")
        name = input()
        print("Введите фамилию преподавателя: ")
        surname = input()
        print("Введите факультет преподавателя: ")
        department = input()
        try:
            add_teacher(name, surname, department)
        except Exception as e:
            print(e)
            print("Ошибка при вводе команд, введите данные снова")
    if user_input == 3:
        print("Введите имя курса: ")
        title = input()
        print("Введите описание курса: ")
        description = input()
        print("Введите id преподавателя курса: ")
        teacher_id = input()
        try:
            add_course(title, description, teacher_id)
        except Exception as e:
            print(e)
            print("Ошибка при вводе команд, введите данные снова")
    if user_input == 4:
        print("Введите дату экзамена: ")
        date = input()
        print("Введите id курса экзамена: ")
        course_id = input()
        print("Введите максимальный бал экзамена: ")
        max_score = input()
        try:
            add_exam(date, course_id, max_score)
        except Exception as e:
            print(e)
            print("Ошибка при вводе команд, введите данные снова")
    if user_input == 5:
        print("Введите id студента оценки: ")
        student_id = input()
        print("Введите id экзамена оценки: ")
        exam_id = input()
        print("Введите оценку: ")
        score = input()
        try:
            add_exam(student_id, exam_id, score)
        except Exception as e:
            print(e)
            print("Ошибка при вводе команд, введите данные снова")

    if user_input == 6:
        print("По какому параметру выбрать для изменения: ")
        update_by = input()
        print("Введите параметр для изменения: ")
        update_param = input()
        print("Введите значение параметра по которому выбрать для изменения: ")
        update_by_value = input()
        print("Введите на что изменить параметр: ")
        update_param_value = input()
        try:
            update_student(update_by, update_param, update_by_value, update_param_value)
        except Exception as e:
            print(e)
            print("Ошибка при вводе команд, введите данные снова")

    if user_input == 7:
        print("По какому параметру выбрать для изменения: ")
        update_by = input()
        print("Введите параметр для изменения: ")
        update_param = input()
        print("Введите значение параметра по которому выбрать для изменения: ")
        update_by_value = input()
        print("Введите на что изменить параметр: ")
        update_param_value = input()
        try:
            update_teacher(update_by, update_param, update_by_value, update_param_value)
        except Exception as e:
            print(e)
            print("Ошибка при вводе команд, введите данные снова")
    
    if user_input == 8:
        print("По какому параметру выбрать для изменения: ")
        update_by = input()
        print("Введите параметр для изменения: ")
        update_param = input()
        print("Введите значение параметра по которому выбрать для изменения: ")
        update_by_value = input()
        print("Введите на что изменить параметр: ")
        update_param_value = input()
        try:
            update_course(update_by, update_param, update_by_value, update_param_value)
        except Exception as e:
            print(e)
            print("Ошибка при вводе команд, введите данные снова")

    if user_input == 9:
        delete_student()
    if user_input == 10:
        delete_course()
    if user_input == 11:
        delete_teacher()
    if user_input == 12:
        delete_exam()

    if user_input == 13:
        print("Введите факультет: ")
        department = input()
        get_students_by_department(department)

    if user_input == 14:
        print("Введите имя параметра преподавателя: ")
        select_by = input()
        print("Введите параметр преподавателя: ")
        select_by_value = input()
        get_courses_by_teacher(select_by, select_by_value)

    if user_input == 15:
        print("Введите имя параметра курса: ")
        select_by = input()
        print("Введите параметр курса: ")
        select_by_value = input()
        get_students_by_course(select_by, select_by_value)
    
    if user_input == 16:
        print("Введите имя параметра курса: ")
        select_by = input()
        print("Введите параметр курса: ")
        select_by_value = input()
        get_students_marks_by_course(select_by, select_by_value)
        
    if user_input == 17:
        print("Введите имя параметра курса: ")
        select_by = input()
        print("Введите параметр курса: ")
        select_by_value = input()
        get_students_avg_mark_by_course(select_by, select_by_value)
    
    if user_input == 18:
        print("Введите имя параметра студента: ")
        select_by = input()
        print("Введите параметр студента: ")
        select_by_value = input()
        get_student_avg_mark(select_by, select_by_value)
        
    if user_input == 19:
        print("Введите факультет: ")
        department = input()
        get_students_avg_mark_by_department(department)

    user_input = int(input())



# add_teacher("Препод Яндекса", "", "ПМИ")
# add_teacher("Препод Т-Банка", "", "ПМИ")
# add_course("Яндекс Кружок", "Олимпиадное программирование", "1")
# add_course("Т-Банк", "Олимпиадное программирование", "2")
# add_student("Student 1", "Surname 1", "ПМИ", "08.03.2000")
# add_student("Student 2", "Surname 2", "ПМИ", "08.03.2000")
# add_student("Student 3", "Surname 3", "ПМИ", "08.03.2000")
# add_teacher("ПМИ Teacher 1", "ПМИ Teacher 1 Surname", "ПМИ")
# # get_students_by_course("title", "Яндекс Кружок")
# add_grade("1", "1", "5")
# add_grade("1", "1", "3")
# add_grade("2", "1", "3")
# add_grade("3", "1", "5")
# get_students_marks_by_course("title", "Яндекс Кружок")
# get_students_avg_mark_by_course("title", "Яндекс Кружок")
# get_students_avg_mark_by_student("name", "Student 1")
# get_students_avg_mark_by_department("ПМИ")

cursor.close()
db_connection.close()
print("\nСоединение с базой данных закрыто.")