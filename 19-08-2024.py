import sqlite3 as sq
list = [(1,"Lucian", "Lindsey", "(07745) 6435470", 2020),\
(2,"Anna", "Riddle", "(036086) 763132", 2019),\
(3,"Zachary", "Guerra", "(07110) 0192114", 2020),\
(4,"Tiger", "Head","(00608) 9633559", 2019),\
(5,"Andrew", "Ramirez","(0754) 50923165", 2019),\
(6,"Orson", "Hodge","(0807) 66180997", 2019),\
(7,"Eric", "Levy","(0573) 11099500", 2019),\
(8,"Jelani", "Buchanan", "(031798) 918995",2019),\
(9,"Chandler", "Francis","(03950) 5230333", 2020),\
(10,"Caleb", "Love" ,"(0177) 47619963",2019),\
(11,"Vaughan", "Fischer", "(037858) 584933", 2019),\
(12,"Kenneth", "Manning","(064) 58255208", 2018),\
(13,"Solomon", "Houston","(046) 90066968", 2020),\
(14,"Amelia", "Cole","(07470) 3567155", 2020)]



with sq.connect('C:/Users/3/Python31/DataBase/Example.db') as cnt:
    cur = cnt.cursor()
#    # Псевдоним
#    #cur.execute('SELECT last_name AS lm FROM Students WHERE lm = "Solo"')
#    #list = cur.fetchall()
#    #for item in list:
#    #    print(item)
#    # Cортировка 
#    cur.execute('SELECT * FROM Students ORDER BY aver DESC') # ASC - по возрастанию DESC - по убыванию
#    list = cur.fetchall()
#    for item in list:
#        print(item)
#    # Условие для значения в поле (колонке)
#    cur.execute('''
#CREATE TABLE IF NOT EXISTS Departments(
#                Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
#                Building INTEGER NOT NULL CHECK(Building >= 1 AND Building <= 5),
#                Financing REAL DEFAULT 0.0 CHECK(Financing >= 0),
#                Name TEXT UNIQUE NOT NULL) ''')
#    cur.execute(''' CREATE TABLE IF NOT EXISTS Diseases( 
#                Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
#                Name TEXT UNIQUE NOT NULL,
#                Severity INTEGER DEFAULT 1 CHECK(Severity >= 1)) ''')
#    
#    cur.execute(''' CREATE TABLE IF NOT EXISTS Doctors( 
#                Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
#                Name TEXT UNIQUE NOT NULL,
#                Surname TEXT UNIQUE NOT NULL,
#                Phone TEXT,
#                Salary REAL NOT NULL CHECK(Salary >= 1))''')
#    cur.execute(''' CREATE TABLE IF NOT EXISTS Examinations( 
#                Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
#                Name TEXT UNIQUE NOT NULL,
#                DayOfWeek INTEGER NOT NULL CHECK( DayOfWeek >= 1 AND DayOfWeek <= 7),
#                StartTime REAL NOT NULL CHECK(StartTime >= 8.0 AND StartTime <= 18.0),
#                EndTime REAL NOT NULL CHECK(EndTime >= 8.0 AND EndTime <= 18.0)) ''')
#    
#    cur.execute(''' CREATE TABLE IF NOT EXISTS Wards( 
#                Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
#                Name TEXT UNIQUE NOT NULL,
#                Building INTEGER NOT NULL CHECK(Building >= 1 AND Building <= 5),
#                Floor INTEGER NOT NULL CHECK(Floor >= 1)) ''')
#    for item in list:
#        #print(item[0])
#        cur.execute('''
#INSERT INTO 'Doctors'  VALUES (?,?,?,?,?)''', (item[0], item[1], item[2], item[3], item[4]))
#        cnt.commit()
#
    ##TASK1 вывод палат
    #cur.execute('SELECT * FROM Wards')
    #list = cur.fetchall()
    #for std in list:
    #    print(std)
    ## Task2
    #cur.execute('SELECT surname, phone FROM Doctors')
    #list = cur.fetchall()
    #for std in list:
    #    print(std)
    ## Task3
    #cur.execute('SELECT DISTINCT Floor FROM Wards')
    #list = cur.fetchall()
    #for std in list:
    #    print(std)
    ## Task4
    #cur.execute('SELECT name AS "Name of Diseases", Severity AS "Sevetity of Diseases" FROM Diseases')
    #list = cur.fetchall()
    #for std in list:
    #    print(std)
    ## Task5
    #cur.execute('SELECT name AS "Name of Diseases", Severity AS "Sevetity of Diseases" FROM Diseases AS "Болезни"')
    #list = cur.fetchall()
    #for std in list:
    #    print(std)
    ## Task6
    #cur.execute('SELECT name FROM Departments WHERE Building = 1 AND Financing > 30000')
    #list = cur.fetchall()
    #for std in list:
    #    print(std)
    ## Task7
    #cur.execute('SELECT name FROM Departments WHERE (Building = 1 OR Building = 3)  AND (Financing > 12000 AND Financing < 15000)')
    #list = cur.fetchall()
    #for std in list:
    #    print(std)
    ## Task8
    #cur.execute('SELECT name FROM Wards WHERE (Building = 1 OR Building = 2)  AND Floor = 1')
    #list = cur.fetchall()
    #for std in list:
    #    print(std)
    ## Task9
    #cur.execute('SELECT name, Financing FROM Departments WHERE (Building = 1 OR Building = 2 OR Building = 3)  AND (Financing < 11000 OR Financing >25000)')
    #list = cur.fetchall()
    #for std in list:
    #    print(std)
        ## Task10
    #cur.execute('SELECT surname FROM Doctors WHERE Salary >= 2020')
    #list = cur.fetchall()
    #for std in list:
    #    print(std)
    ## Task12
    #cur.execute('SELECT DISTINCT name FROM Examinations WHERE DayOfWeek <=3 AND StartTime >=10 ')
    #list = cur.fetchall()
    #for std in list:
    #    print(std)
        ## Task13
    #cur.execute('SELECT name, Building FROM Wards WHERE (Building = 1 OR Building = 3)')
    #list = cur.fetchall()
    #for std in list:
    #    print(std)
            ## Task14
    #cur.execute('SELECT name FROM Diseases WHERE Severity > 2')
    #list = cur.fetchall()
    #for std in list:
    #    print(std)
            ## Task15
    #cur.execute('SELECT name, Building FROM Wards WHERE (Building <> 1 AND Building <> 3)')
    #list = cur.fetchall()
    #for std in list:
    #    print(std)
                ## Task16
    #cur.execute('SELECT name FROM Departments WHERE (Building = 1 OR Building = 3)')
    #list = cur.fetchall()
    #for std in list:
    #    print(std)
        ## Task17
    #cur.execute('SELECT name, surname FROM Doctors WHERE surname LIKE "F%"')
    #list = cur.fetchall()
    #for std in list:
    #    print(std)