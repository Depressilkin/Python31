##task3
#class Animal:
#    pass
#    def __init__(self, name, nickname, weight, wool = None, voice = None):
#        self.name = name
#        self.nickname = nickname
#        self.weight = weight
#        if wool != None:
#            self.wool = True
#        else:
#            self.wool = False
#        if voice != None:
#            self.voice = voice
#        else:
#            self.voice = None
#    
#    def get_nickname(self):
#        return self.nickname
#    def __str__(self):
#        if self.voice != None:
#            return f'{self.voice *3}'
#        else:
#            return None
##
#class Giraff(Animal):
#    def __init__(self, name, nickname, weight, wool = None, voice = None):
#        super().__init__(name, nickname, weight, wool, voice)
#    def get_nickname(self):
#        return super().get_nickname()
#    def get_voice(self):
#        return super().get_voice()
#
#obj1 = Giraff('Giraff', 'Melman', 1.9, True, 'mu-u')
#print(obj1.__dict__, obj1.get_nickname(), obj1)
#
#class Hypo(Animal):
#    def __init__(self, name, nickname, weight, wool = None, voice = None):
#        super().__init__(name, nickname, weight, wool, voice)
#    def get_nickname(self):
#        return super().get_nickname()
#    def get_voice(self):
#        return super().get_voice()
#
#obj2 = Hypo('Hypo', 'Glory', 1.5)
#print(obj2.__dict__, obj2.get_nickname(), obj2.get_voice())
#
#class Lion(Animal):
#    def __init__(self, name, nickname, weight, wool = None, voice = None):
#        super().__init__(name, nickname, weight, wool, voice)
#    def get_nickname(self):
#        return super().get_nickname()
#    def get_voice(self):
#        return super().get_voice()

#obj3 = Lion('Lion', 'Alex', 200, True, 'r-r-r')
#print(obj3.__dict__, obj3.get_nickname(), obj3.get_voice())

##Магические методы
#class Digit:
#    def __init__(self, vol):
#        self.vol = vol
#    # математические операторы
#    def __add__(self, other): # магический метод на сценарий суммы
#        if isinstance(other, Digit):
#            return self.vol + other.vol
#        else:
#            print('Нужен второй объект для суммы')
#    def __sub__(self, other): # магический метод на сценарий разности
#        if isinstance(other, Digit):
#            return self.vol - other.vol
#        else:
#            print('Нужен объект для вычитаемого')
#    def __mul__(self, other): # магический метод на сценарий умножения
#        if isinstance(other, Digit):
#            return self.vol * other.vol
#        else:
#            print('Нужен объект произведения')        
#    # логические операторы lt, gt, le, ge, eq
#    def __lt__(self, other):
#        if isinstance(other, Digit):
#            return self.vol < other.vol
#    def __gt__(self, other):
#        if isinstance(other, Digit):
#            return self.vol > other.vol
#    def __le__(self, other):
#        if isinstance(other, Digit):
#            return self.vol <= other.vol
#    def __eq__(self, other):
#        if isinstance(other, Digit):
#            return self.vol == other.vol
#_null = Digit(1)
#_one = Digit(1)
#print(_null + _one)
#print(_null - _one)
#print(_null * _one)
#print(_null < _one)
#print(_null == _one)

#task 1
#class Num:
#    def __init__(self,volue):
#        self.volue = volue
#    def __add__(self, other):
#        if isinstance(other, Num):
#            return self.volue + other.volue
#        else:
#            return self.volue + other
#    def __sub__(self,other):
#        if isinstance(other, Num):
#            return self.volue - other.volue
#        else:
#            return self.volue - other
#    def __mul__(self, other):
#        if isinstance(other, Num):
#            return self.volue * other.volue
#        else:
#            return self.volue * other
#    def __truediv__(self, other):
#        if isinstance(other, Num):
#            return (self.volue / other.volue)
#        else:
#            return self.volue / other
#object1 = Num(5)
#object2 = Num(23)
#var = 34
#print(object1 + object2, object1 + var, object1 - object2, object1 - var, )
#print(object1 * object2, object1 * var, object1 / object2, object1 / var )

#task2
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
#    def __add__(self, other):
#        if isinstance(other, Fraction):
#            self.com_denominator = self.denominator * other.denominator
#            self.com_numenator = self.numerator * other.denominator + self.denominator * other.numerator
#            self.reduce()
#            return f'{self.com_numenator}/{self.com_denominator}'
#
#    def __sub__(self, other):
#        self.com_denominator = self.denominator * other.denominator
#        self.com_numenator = self.numerator * other.denominator - self.denominator * other.numerator
#        self.reduce()
#        return f'{self.com_numenator}/{self.com_denominator}'
#
#    def __mul__(self, other):
#        self.com_denominator = self.denominator * other.denominator
#        self.com_numenator = self.numerator * other.numerator
#        self.reduce()
#        return f'{self.com_numenator}/{self.com_denominator}'
#
#    def __truediv__(self, other):
#        self.com_denominator = self.denominator * other.numerator
#        self.com_numenator = self.numerator * other.denominator
#        self.reduce()
#        return f'{self.com_numenator}/{self.com_denominator}'
#
#    def reduce(self):
#        for nod in range(max(self.com_denominator, self.com_numenator), 0, -1):
#            if self.com_denominator % nod == 0 and self.com_numenator % nod == 0:
#                self.com_denominator //= nod
#                self.com_numenator //= nod
#                break
#
#object1 = Fraction(3,5)
#object2 = Fraction(2, 5)
#print(object1 + object2)
#print(object1 - object2)
#print(object1 * object2)
#print(object1 / object2)
# task3
class Lib:
    def __init__(self, counter):

        self.counter = counter
    def __iadd__(self, other):
        self.counter += other
        return f'после добавления количество книг: {self.counter}'
    def __isub__(self, other):
        self.counter -= other
        return f'после уменьшения количество книг: {self.counter}'
    def __lt__(self,other):
        if isinstance(other, Lib):
            if self.counter < other.counter:
                return f'в нашей баблиотеке книг меньше'
    def __gt__(self,other):
        if isinstance(other, Lib):
            if self.counter > other.counter:
                return f'в нашей баблиотеке книг больше'
    def __eq__(self,other):
        if isinstance(other, Lib):
            if self.counter == other.counter:
                return f'книг одинаково'
    def __le__(self,other):
        if isinstance(other, Lib):
            if self.counter <= other.counter:
                return f'в нашей баблиотеке книг не меньше'
o1 = Lib(200)
o2 = Lib(188)
print(o1 > o2)

    