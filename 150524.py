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
#class Person:
#    def __init__(self):
#        self.first_name = input('Введите фамилия')
#        self.second_name = input('Введите имя')
#        self.dob = input('Введите дату рождения')
#        self.mob = input('Введите мобильный номер')
#        self.country = input('Введите страну')
#        self.city = input('Введите город')
#        self.home_address = input('Введите домашний адрес')
#    def print_info(self, name_key,id):
#        if name_key == 'Имя' or name_key =='1' or name_key == '3':
#            print(f'Имя: {bd[id].first_name}')
#        if name_key == 'Фамиля' or name_key =='2' or name_key == '3':
#            print(f'Фамилия: {bd[id].second_name}')
#        if name_key == 'Дата рождения' or name_key =='3' or name_key == '3':
#            print(f'Дата рождения: {bd[id].dob}')
#        if name_key == 'Мобильный номер' or name_key =='4' or name_key == '3':
#            print(f'Мобильный номер: {bd[id].mob}')
#        if name_key == 'Страна' or name_key =='5' or name_key == '3':
#            print(f'Страна: {bd[id].country}')
#        if name_key == 'Город' or name_key =='6' or name_key == '3':
#            print(f'Город: {bd[id].city}')
#        if name_key == 'Домашний адрес' or name_key =='7' or name_key == '3':
#            print(f'Домашний адрес: {bd[id].home_address}')
#        else:
#            print('Некорректный ввод')
#    def change_info(self,name_key, id):
#        if name_key == 'Имя' or name_key =='1':
#            bd[id].first_name = input("Введите новое Имя")
#        elif name_key == 'Фамиля' or name_key =='2':
#            bd[id].second_name_name = input("Введите новую Фамилию")
#        elif name_key == 'Мобильный номер' or name_key =='4':
#            bd[id].mob = input("Введите новый мобильный номер")
#        elif name_key == 'Домашний адрес' or name_key =='7':
#            bd[id].home_address = input("Введите новый адрес")
#        else:
#            print('Некорректный ввод')
#
#bd = {}
#while True:
#    print(bd)
#    menu_choise = input(f'Меню:\n1 просмотр информации\n2 изменение информации\n3 Вывод всех данных\n4 добавить человека\n0 Выход')
#    if menu_choise == '0':
#        break
#    id = input('Введите ID человека')
#    if menu_choise == '1':
#        name_key = input('Введите поля для просмотра:\n1- Имя\n2- Фамилия\n3- Дата рождения\n4- Мобильный номер\n5- Страна\n6- Город\n7-Домашний адрес')
#        bd[id].print_info(name_key, id)
#    elif menu_choise == '2':
#        name_key = input('Введите поля для изменения:\n1- Имя\n2- Фамилия\n3- Дата рождения\n4- Мобильный номер\n5- Страна\n6- Город\n7-Домашний адрес')
#        bd[id].change_info(name_key, id)
#    elif menu_choise == '3':
#        bd[id].print_info(menu_choise, id)
#    elif menu_choise == '4':
#        bd[id] = Person()

#инкапсуляция (возможность скрыть информацию о классе для объектов класса)

#1 процедурный
stack = []
def app(list, item):
    list.append(item)
    return list
def rmv(list):
    list.pop()
    return list
app(stack,12)
app(stack,1)
app(stack,11)
print(stack)
rmv(stack)
print(stack)

## 2 объектный
#class Stack:
#    def __init__(self):
#        self.stack_list = []
#        self.sum = 0
#    def app(self, stack_list, item):
#        self.sum += item
#        self.stack_list.append(item)
#        return self.stack_list
#    def rmv(self,stack_list):
#        self.sum -= self.stack_list[-1]
#        self.stack_list.pop()
#        return self.stack_list
#    
#obj = Stack()
#obj.app(obj.stack_list,21)
#obj.app(obj.stack_list,43)
#print(obj.stack_list, obj.sum)
#
#obj2 = Stack()
#obj2.app(obj.stack_list,1)
#obj2.app(obj.stack_list,4)
#obj2.app(obj.stack_list,6)
#print(obj2.stack_list,obj2.sum)

# Наследование
## переменные класса
#class ExCl:
#    counter = 0
#    def __init__(self, arg=1) :
#        self.var = arg
#        ExCl.counter +=1
#
#obj1 = ExCl()
#obj2 = ExCl(2)
#obj3 = ExCl(23)
#print(f'Значение переменной экземпляра var: {obj1.var}, {obj2.var}, {obj3.var}\n переменная класса:{ExCl.counter}')
#
###переменная экземпляра
#print(obj1.__dict__, obj2.__dict__)
##Создайте класс «Дробь». Необходимо хранить в полях
#класса: числитель и знаменатель. Реализуйтеметодыкласса
#для ввода данных, вывода данных, реализуйте доступ к
#отдельным полям через методы класса. Также создайте
#методы класса для выполнения арифметических операций (сложение, вычитание, умножение, деление, и т.д.).
#task4
#class Fraction:
#    def __init__(self,numerator,denominator):
#        self.numerator = numerator
#        self.denominator = denominator
#    
#    def change(self):
#        self.numerator = input('Введите новый числитель')
#        self.denominator = input('Введите новый знаменатель')
#    
#    def output(self):
#        print(f'{self.numerator}/{self.denominator}')
#    
#    def get_numerator(self):
#        return self.numerator
#    
#    def get_denominator(self):
#        return self.denominator
#    
#    def summ(self):
#        a = int(input('Введите числитель второго слагаемого'))
#        b = int(input('Введите знаменатель второго слагаемого'))
#        self.com_denominator = self.denominator * b
#        self.com_numenator = self.numerator * b + a * self.denominator
#        self.reduce()
#
#    def substraction(self):
#        a = int(input('Введите числитель второго слагаемого'))
#        b = int(input('Введите знаменатель второго слагаемого'))
#        self.com_denominator = self.denominator * b
#        self.com_numenator = self.numerator * b - a * self.denominator
#        self.reduce()
#
#    def multiplication(self):
#        c = int(input('Введите числитель второго множителя'))
#        d = int(input('Введите знаменатель второго множителя'))
#        self.com_denominator = self.denominator * d
#        self.com_numenator = self.numerator * c
#        self.reduce()
#
#    def division(self):
#        c = int(input('Введите числитель делителя'))
#        d = int(input('Введите знаменатель делителя'))
#        self.com_denominator = self.denominator * c
#        self.com_numenator = self.numerator * d
#        self.reduce()
#
#    def reduce(self):
#        for nod in range(max(self.com_denominator, self.com_numenator), 0, -1):
#            if self.com_denominator % nod == 0 and self.com_numenator % nod == 0:
#                self.com_denominator //= nod
#                self.com_numenator //= nod
#                break
#        self.numerator = self.com_numenator
#        self.denominator = self.com_denominator
#
#obj1 = Fraction(3,4)
##obj1.output()
##print(f'Числитель:{obj1.get_numerator()}\nЗнаменатель:{obj1.get_denominator()}')
##obj1.change() 
##obj1.output()
#obj1.substraction()
#obj1.output()
#
#
# полиморфизм
# I перегруженный метод с разным типом данных
class Auto:
    def __init__(self,maker,model):
        self.maker = maker
        self.model = model

    def get_model(self):
        return self.model
    def __str__(self):

        return f'Auto {self.maker}, {self.model}'
bmw = Auto('BMW','X4')
print(bmw)

#II перегруженный метод c разным количеством агрументов
class Figure:
    def __init__(self, a=None, b=None, c=None, d=None):
        if a != None and b != None and c != None and d != None:
            print('Вывод 4угольника abcd')
        elif a != None and b != None and c != None:
            print('Вывод 3угольника abc')
        elif a != None and b != None:
            print('Вывод отрезка')
        else:
            print('вывод с 1 или 0 аргументов')
    def f(*arg):
        pass
obj1 = Figure()
obj2 = Figure(2,3,4)
obj3 = Figure(3,4,5,6)
