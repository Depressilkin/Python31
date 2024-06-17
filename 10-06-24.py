# task 2
#class Doors:
#    def __init__(self, color, count, size):
#        self.color_doors = color
#        self.count_doors = count
#        self.size_doors = size
#
#class Wheels:
#    def __init__(self, count, size):
#        self.count_wheels = count
#        self.size_wheels = size
#
#class Body:
#    def __init__(self, color, size, type):
#        self.color_body = color
#        self.size_body = size
#        self.type_body = type
#
#class Engine:
#    def __init__(self, type, spend, power, size):
#        self.type_engine = type
#        self.spend = spend
#        self.power = power
#        self.size_engine = size
#    
#    def __str__(self):
#        return 'wru-wru'
#    
#    
#class Auto(Doors, Wheels, Body, Engine):
#    def __init__(self, model, made,  type_engine, spend_engine, power_engine, size_engine, color_body, size_body, type_body, count_wheels, size_wheels, color_doors, count_doors, size_doors):
#        self.model = model
#        self.made = made
#        Engine.__init__(self, type_engine, spend_engine, power_engine, size_engine)
#        Body.__init__(self, color_body, size_body, type_body)
#        Wheels.__init__(self, count_wheels, size_wheels)
#        Doors.__init__(self, color_doors, count_doors, size_doors)
#    
#    def get_engine(self):
#        return self.power
#    
#    def get_color_body(self):
#        return self.color_body
#    
#    def __str__(self):
#        return Engine.__str__(self)
#    
#    def get_spend_fuel(self, s):
#        return int(self.spend) * int(s) / 100 
#
#auto1 = Auto('X5','BMW', 'V6', 10, '100', '600x1400', 'red', '2500x2200', 'cross', '4', "'24", 'red', '5', '1300x1000')
#print(auto1.__dict__, auto1.get_color_body())
#print(auto1, auto1.get_spend_fuel(50))

# task 1

#from math import pi
#class Rectangle:
#    def __init__(self, a, b):
#        self.a = a
#        self.b = b
#
#    def get_S_rectangle(self):
#        return self.a * self.b 
#
#class Circle:
#    def __init__(self, r):
#        self.r = r
#    def get_S_circle(self):
#        return pi * self.r ** 2
#
#class Cinrect(Rectangle, Circle):
#    def __init__(self, a, b, r):
#        Rectangle.__init__(self, a, b)
#        Circle.__init__(self, r)
#    
#    def get_S_rectangle(self):
#        return super().get_S_rectangle()
#    def get_S_circle(self):
#        return super().get_S_circle()
#    def get_P_summ(self):
#        return (self.a + self.b) * 2 + 2 * pi * self.r
#    def get_S_negative(self):
#        return  self.a * self.b - pi * self.r ** 2
#obj1 = Cinrect(20,30, 10)
#print(obj1.__dict__)
#print(obj1.get_S_negative(), obj1.get_S_circle(), obj1.get_S_rectangle() )
#

# Декорирование функции
#def f():
#    return 'Hello, World'
#
#def f2(func):
#    print('Какое-то неважное дело')
#    func()
#    print('Какое-то неважное дело')
#
#def f3():
#    print('Какое-то важное действие')
#@f2
#def f4():
#    print('Какое-то совсем неважное дело')
##var2 = f2(f4)
#var2 = f4
#print(var2)
# task 1
#from datetime import datetime
#def func_decorator():
#    def get_current_time():
#        cur_date = datetime.now()
#        cur_time = cur_date.strftime('%H:%M')
#        return cur_time
#    print('*'*8)
#    print(get_current_time())
#    print('*'*8)
#func_decorator()

# task 2
#def func_decorator():
#    def get_current_time():
#        cur_date = datetime.now()
#        cur_time = cur_date.strftime('%H:%M')
#        return cur_time
#    def pattern():
#        return f'||'
#    return f'{'*' * 8}\n{pattern()}{get_current_time()}{pattern()}\n{'*' * 8}'
#print(func_decorator())

# task 3
#from datetime import datetime
#def func_decorator(f):
#    print('*'*8)
#    print(f())
#    print('*'*8)
#
#@func_decorator
#def get_current_time():
#    cur_date = datetime.now()
#    cur_time = cur_date.strftime('%H:%M')
#    return cur_time
#
#get_current_time
def f_decor(f):
    return f'Основа, соус, {f()}'
@f_decor
def margo():
    return f'томат, лук, сыр'
@f_decor
def four_cheese():
    return f'сыр, сыр, и еще раз сыр'
@f_decor
def hawaii():
    return f'сыр, ананас'
choice = input(f'Выберите пиццу:\n1 - Маргарита\n2 - Четыре сыра\n3 - Гавайская')
if choice == '1':
    print(margo)
elif choice == '2':
    print(four_cheese)
elif choice == '3':
    print(hawaii)
