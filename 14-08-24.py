import sqlite3 as sq
stud_list = [(1, 'Alex', 'Smith', 'London', 'Eng', '12.12.1991', 'alex@mail.ru', '7-33-34', 4.3, 'Programmer', 'Design'),
                 (2, 'Lee', 'Ramsey', 'London', 'Eng', '19.10.1991', 'lee@mail.ru', '7-93-30', 3.3, 'Design', 'Programmer'),
                 (3, 'Aaron', 'Drogba', 'Cardiff', 'Eng', '15.10.1990', 'aaron@mail.ru', '7-93-90', 3.8, 'Design', 'Tester'),
                 (4, 'Samir', 'Zizy', 'Paris', 'Fra', '15.12.1990', 'samir@mail.ru', '7-93-97', 4.8,  'Tester', 'Design'),
                 (5, 'Roy', 'Zizy', 'Paris', 'Fra', '15.12.1992', 'roy@mail.ru', '7-93-97', 4.6,  'Tester', 'Design'),
                 (6, 'Clement', 'Solo', 'Can', 'Fra', '15.12.1992', 'clem@mail.ru', '7-93-91', 4.4,  'Programmer', 'Tester'),
                 (7, 'Anna', 'Solo', 'Can', 'Fra', '15.12.1990', 'anna@mail.ru', '7-93-91', 3.1,  'Design', 'Programmer'),
                 ]

with sq.connect('C:/Users/3/Python31/DataBase/Example.db') as cnt:
    cur = cnt.cursor()
    #cur.execute('''CREATE TABLE IF NOT EXISTS Students(
    #            id INTEGER PRIMARY KEY,
    #            first_name TEXT NOT NULL,
    #            last_name TEXT NOT NULL,
    #            city TEXT NOT NULL,
    #            country TEXT NOT NULL,
    #            bday TEXT NOT NULL,
    #            email TEXT NOT NULL,
    #            phone_number TEXT NOT NULL ,
    #            aver REAL NOT NULL,
    #            max_course TEXT NOT NULL,
    #            min_course TEXT NOT NULL
    #            )''')
    #for student in stud_list:
    #    cur.execute('''INSERT INTO Students VALUES(?,?,?,?,?,?,?,?,?,?,? )''', student)
    #    cnt.commit()
    #TASK1 запрос на вывод имя-фамилия с оценкой от 3.2 до 4.7
    #cur.execute('SELECT first_name, last_name FROM STUDENTS WHERE aver >3.2 and aver < 4.7')
    #list = cur.fetchall()
    #print('Список студентов:')
    #for student in list:
    #    print(f'Имя: {student[0]} Фамилия: {student[1]}')
    #TASK2 33 и страше
    #cur.execute('SELECT first_name, last_name , bday FROM STUDENTS')
    #list = cur.fetchall()
    #for student in list:
    #    if int(student[2][-4:]) <1991 or ((int(student[2][-4:]) == 1991) and (int(student[2][-7:-5]) < 8)):
    #        print(f'Имя: {student[0]} Фамилия: {student[1]}')
    #TASK3 с 90 по 92
    #cur.execute('SELECT first_name, last_name , bday FROM STUDENTS')
    #list = cur.fetchall()
    #for student in list:
    #    if int(student[2][-4:]) >= 1990 and int(student[2][-4:]) <= 1991:
    #        print(f'Имя: {student[0]} Фамилия: {student[1]}')
    #TASK4 однофамильцы SOLO
    #cur.execute(''' SELECT first_name, last_name FROM Students WHERE last_name = "Solo" ''')
    #list = cur.fetchall()
    #for student in list:
    #    print(student[0], student[1] )
    #TASK5 ищем 2 и более "3" в номере телефона
    #cur.execute('SELECT * FROM STUDENTS WHERE phone_number LIKE "%3%3%"')
    #list = cur.fetchall()
    #for student in list:
    #    print(student[0], student[1] )
    #TASK6 поиск почты на букву "а"
    #cur.execute('SELECT * FROM Students WHERE email LIKE "a%"')
    #list = cur.fetchall()
    #for std in list:
    #    print(std)
    #TASK 7 поиск мин сред
    #cur.execute('SELECT first_name, last_name, MIN(aver) FROM Students')
    #list = cur.fetchall()
    #for std in list:
    #    print(std)
    #TASK 8 поиск мax сред
    #cur.execute('SELECT first_name, last_name, MAX(aver) FROM Students')
    #list = cur.fetchall()
    #for std in list:
    #    print(std)
    #TASK 9 
    #cur.execute('SELECT DISTINCT city FROM Students ')
    #list = cur.fetchall()
    #for std in list:
    #    print(std)
    # TASK 10
    #cur.execute('SELECT max_course, COUNT(*) FROM Students WHERE max_course = "Design" GROUP BY max_course ')
    #list = cur.fetchall()
    #for item in list:
    #    print(item)
    # TASK 11
    #cur.execute('SELECT AVG(aver) FROM Students')
    #list = cur.fetchall()
    #for item in list:
    #    print(item)