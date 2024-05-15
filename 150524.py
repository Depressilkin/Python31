# объявление класса
#class FirstClass:
#    firs_var = 1
#    "Мой первый класс"
#    def __init__(self):
#        print(self)
#        pass
#    pass
#print(FirstClass.firs_var)
# способ создания экземпляра класса (объекта)
#first_expl = FirstClass()
#print(first_expl.__dict__)
#first_expl.color = 'red'
#print(first_expl.color)
#second_expl = FirstClass()
#second_expl.color = 'black'
#print(second_expl.color)
#print(first_expl, first_expl.__init__)
#class Cats:
#    def __init__(self):
#        self.name = input('Введите имя котёнка')
#        self.age = input('Введите возраст')
#my_cat = Cats()
#print(my_cat.name)
#print(Cats.__dict__)
class Person:
    def __init__(self):
        self.first_name = input('Введите фамилия')
        self.second_name = input('Введите имя')
        self.dob = input('Введите дату рождения')
        self.mob = input('Введите мобильный номер')
        self.country = input('Введите страну')
        self.city = input('Введите город')
        self.home_address = input('Введите домашний адрес')
    def print_info(self, name_key,id):
        if name_key == 'Имя' or name_key =='1' or name_key == '3':
            print(f'Имя: {bd[id].first_name}')
        if name_key == 'Фамиля' or name_key =='2' or name_key == '3':
            print(f'Фамилия: {bd[id].second_name}')
        if name_key == 'Дата рождения' or name_key =='3' or name_key == '3':
            print(f'Дата рождения: {bd[id].dob}')
        if name_key == 'Мобильный номер' or name_key =='4' or name_key == '3':
            print(f'Мобильный номер: {bd[id].mob}')
        if name_key == 'Страна' or name_key =='5' or name_key == '3':
            print(f'Страна: {bd[id].country}')
        if name_key == 'Город' or name_key =='6' or name_key == '3':
            print(f'Город: {bd[id].city}')
        if name_key == 'Домашний адрес' or name_key =='7' or name_key == '3':
            print(f'Домашний адрес: {bd[id].home_address}')
        else:
            print('Некорректный ввод')
    def change_info(self,name_key, id):
        if name_key == 'Имя' or name_key =='1':
            bd[id].first_name = input("Введите новое Имя")
        elif name_key == 'Фамиля' or name_key =='2':
            bd[id].second_name_name = input("Введите новую Фамилию")
        elif name_key == 'Мобильный номер' or name_key =='4':
            bd[id].mob = input("Введите новый мобильный номер")
        elif name_key == 'Домашний адрес' or name_key =='7':
            bd[id].home_address = input("Введите новый адрес")
        else:
            print('Некорректный ввод')

bd = {}
while True:
    print(bd)
    menu_choise = input(f'Меню:\n1 просмотр информации\n2 изменение информации\n3 Вывод всех данных\n4 добавить человека\n0 Выход')
    if menu_choise == '0':
        break
    id = input('Введите ID человека')
    if menu_choise == '1':
        name_key = input('Введите поля для просмотра:\n1- Имя\n2- Фамилия\n3- Дата рождения\n4- Мобильный номер\n5- Страна\n6- Город\n7-Домашний адрес')
        bd[id].print_info(name_key, id)
    elif menu_choise == '2':
        name_key = input('Введите поля для изменения:\n1- Имя\n2- Фамилия\n3- Дата рождения\n4- Мобильный номер\n5- Страна\n6- Город\n7-Домашний адрес')
        bd[id].change_info(name_key, id)
    elif menu_choise == '3':
        bd[id].print_info(menu_choise, id)
    elif menu_choise == '4':
        bd[id] = Person()


