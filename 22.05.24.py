#перегруженные методы
class Figure:
    def __init__(self, a = None, b = None, c = None):
        if a != None and b != None and c != None:
            print('Введена информация для треугольника')
        elif a != None and b != None:
            print('Введена информация для отрезка')
        elif a != None:
            print('Введена информация для точки')
        else:
            print("Ни один аргумент не указан")
    def P(self, *arg):
        print(f'Указано {len(arg)} сторон')
        print(f'Периметр фигуры равен {sum(arg)}')

obj1 = Figure()
obj1.P(2,3)
obj2 = Figure()
obj2.P(34,6,8,9)

#Суперклассы и субклассы(подклассы)
#class Animal:
#    pass
#class Manky(Animal):
#    pass
#class Gibbon(Manky):
#    pass
#
#class Super:
#    def __init__(self):
#        self.super_var = 1
#
#
#class Sub(Super):
#    def __init__(self):
#        super().__init__()
#        self.sub_var = 0
#obj1 = Super()
#obj2 = Sub()
#print(f'{obj1.super_var}\n{obj2.sub_var}')
#obj2.super_var = 5
#print(f'{obj1.__dict__}\n{obj2.__dict__}')
##Создайте класс Human, который будет содержать
##информацию о человеке.
##Спомощью механизма наследования, реализуйте класс
##Builder (содержит информацию о строителе), класс Sailor
##(содержит информацию о моряке), класс Pilot (содержит
##информацию о летчике).
##Каждый из классов должен содержать необходимые
##для работы методы.
##атр:супер класс ФИ, возраст, опыт работы методы доступ к поля return атр.
##атр: суб пройденное расстояние (для пилота и моряка), инструменты (для строителя и моряка), методы подсчет
## среднего расстояния (моряк, пило), метод проверки наличия инструмента(моряк, строитель)
#class Human:
#    def __init__(self, name, age, exp):
#        self.name = name
#        self.age = age
#        self.exp = exp
#    def get_name(self):
#        return self.name
#    def get_age(self):
#        return self.age
#    def get_exp(self):
#        return self.exp
#    
#    def set_list_way(self,*way):
#        self.list_way = way
#        return self.list_way
#    def set_list_tools(self,*tools):
#        self.list_tools = tools
#        return self.list_tools
#
#    def get_averege_way(self):
#        self.average_way = sum(self.list_way)/len(self.list_way)
#        return f'Среднее расстояние в пути {self.average_way}'
#    
#    def get_check_tools(self):
#        self.found_tools = input('Введите название инструмента')
#        if self.found_tools in self.list_tools:
#            return f'Есть такой инструмент'
#        else:
#            return 'нет такого инструмента или инструмент введен неверно'
#class Builder(Human):
#    def __init__(self, name, age, exp):
#        super().__init__(name, age, exp)
#    def set_list_tools(self, *tools):
#        return super().set_list_tools(*tools)
#    def get_check_tools(self):
#        super().get_check_tools()
#
#class Sailor(Human):
#    def __init__(self,name, age, exp):
#        super().__init__(name, age, exp)
#    def set_list_tools(self, *tools):
#        return super().set_list_tools(*tools)
#    def set_list_way(self, *way):
#        return super().set_list_way(*way)
#    def get_averege_way(self):
#        return super().get_averege_way()
#    def get_check_tools(self):
#        return super().get_check_tools()
#
#class Pilot(Human):
#    def __init__(self,name, age, exp):
#        super().__init__(name, age, exp)
#    def set_list_way(self, *way):
#        return super().set_list_way(*way)
#    def get_averege_way(self):
#        return super().get_averege_way(self)
#
#person = Human('Max',23,5)
##person.set_list_way(17,47,101)
##print(person.get_averege_way())
##person.set_list_tools('молоток', 'пила', 'дрель')
##person.get_check_tools()
#person2 = Builder('Max',34,5)
#person2.set_list_way(23,34,65,78)
#print(person2.__dict__)
#person3 = Sailor('Alex',65,43)
#person3.set_list_tools('отвертка', 'дрель')
#person3.set_list_way(43,54,76,987)
#print(person3.__dict__)
#print(person3.get_averege_way())
#print(person3.get_check_tools())
#Создайте класс Passport (паспорт), который будет
#содержать паспортную информацию о гражданине заданной страны.
#С помощью механизма наследования, реализуйте
#класс ForeignPassport (загран.паспорт) производный от
#Passport.
#Напомним, что заграничный паспорт содержит помимо паспортных данных, также данные о визах, номер
#заграничного паспорта.
#Каждый из классов должен содержать необходимые
#методы.
#class Passport:
#    def __init__(self, first_name, second_name, dob, country,series,number):
#        self.first_name = first_name
#        self.second_name = second_name
#        self.dob = dob
#        self.country = country
#        self.series = series
#        self.number = number
#    
#class  ForeignPassport(Passport):
#    def __init__(self, first_name, second_name, dob, country, series, number):
#        super().__init__(first_name, second_name, dob, country, series, number)
#        self.list_visa = []
#        self.visa = None
#        self.set_list_visa()
#        self.namber_fp = input('Введите номер загран.паспорта')
#    def set_list_visa(self):
#        while True:
#            visa = input('Введите визу или 0 для выхода')
#            if visa =='0':
#                break 
#            self.list_visa.append(visa)
#
#obj1 = ForeignPassport(1,2,3,4,5,6)
#print(obj1.__dict__)

class Fraction:
    counter = 0
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.counter += 1
    
    def change(self):
        self.numerator = input('Введите новый числитель')
        self.denominator = input('Введите новый знаменатель')
    
    def output(self):
        print(f'{self.numerator}/{self.denominator}')
    
    def get_numerator(self):
        return self.numerator
    
    def get_denominator(self):
        return self.denominator
    
    def summ(self):
        a = int(input('Введите числитель второго слагаемого'))
        b = int(input('Введите знаменатель второго слагаемого'))
        self.com_denominator = self.denominator * b
        self.com_numenator = self.numerator * b + a * self.denominator
        self.reduce()

    @staticmethod
    def counter_ex():
        print(f'Cоздано {Fraction.counter} экземпляров класса')

o1 = Fraction(2,3)
Fraction.counter_ex()
o2 = Fraction(2,3)
o3 = Fraction(2,3)
Fraction.counter_ex()
