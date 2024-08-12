import sqlite3 as sq
with sq.connect('C:/Users/3/Python31/DataBase/Example.db') as cnt:
    cur = cnt.cursor()
    #cоздание таблицы
    #cur.execute('''CREATE TABLE IF NOT EXISTS Address(
    #            id INTEGER PRIMARY KEY,
    #            name TEXT NOT NULL)''')
    #переименование таблицы
    #cur.execute('''ALTER TABLE Address RENAME TO Journal''')
    #добавление записи в таблицу
    #cur.execute('''INSERT INTO Journal(id, name) VALUES(1,"Anna")''')
    #cur.execute('''INSERT INTO Journal(id, name) VALUES(?, ?)''',(2,"Margo"))
    #УДАЛЕНИЕ ПО ID = 1
    #cur.execute('DELETE FROM Journal WHERE id = 1')
    #OБНОВЛЕНИЕ
    #cur.execute('UPDATE Journal SET name = "Anna" WHERE name = "Margo"')
    #ВЫВОД информации
    #SELECT * FROM 'Оценки студентов'
    #cnt.commit()
    ##TASK1
    #cur.execute('SELECT * FROM "Оценки студентов"')
    #students = cur.fetchall()
    #for student in students:
    #    render = {'ID': student[0],
    #              'Name': student[1],
    #              'Email': student[2],
    #              'Age': student[3],
    #              'Group':student[4],
    #              'Aver': student[5],
    #              'Course':student[6]}
    #    #print(render)
    ##TASK 2
    #    #print(render['Name']) 
    ## TASK 3
    #    #print(render['Aver'])
    ## TASK 4
    #cur.execute('SELECT Name, aver FROM "Оценки студентов" WHERE aver > 4')
    #students = cur.fetchall()
    #for student in students:
    #    print(f'Имя: {student[0]}, оценка: {student[1]}')
    #TASK 5
    #cur.execute(''' SELECT DISTINCT cours FROM "Оценки студентов"''')
    #courses = cur.fetchall()
    #for course in courses:
    #    print(course[0])


    cur.execute('SELECT Name, aver FROM "Оценки студентов" WHERE aver <> 3.8')
    students = cur.fetchall()
    for student in students:
        print(f'Имя: {student[0]}, оценка: {student[1]}')