class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
  
    def plus(self):
        return self.a + self.b
  
    def minus(self):
        return self.a - self.b
  
    def multiply(self):
        return self.a * self.b
  
    def div(self):
        if self.b != 0:
            return self.a / self.b
        
    def min(self):
        return min(self.a , self.b)
  
    def max(self):
        return max(self.a , self.b)
    
    def degree(self):
        return self.a ** self.b  
    
    def percent(self):
        return self.a * self.b / 100

class Calendary:
    def __init__(self, day) -> None:
        self.day = day

    def get_weekday(self):
        week = ['Mo','Tu','We', 'Th', 'F', 'Su', 'Sa']
        return week[self.day]
#o1 = Culc(2, 2)
#print(o1.add())
#o2 = Calendary(3)
#print(o2.get_weekday())

class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def change(self):
        self.numerator = input('Введите новый числитель')
        self.denominator = input('Введите новый знаменатель')
    
    def output(self):
        print(f'{self.numerator}/{self.denominator}')
    
    def get_numerator(self):
        return self.numerator
    
    def get_denominator(self):
        return self.denominator
    
    def __add__(self, other):
        if isinstance(other, Fraction):
            self.com_denominator = self.denominator * other.denominator
            self.com_numenator = self.numerator * other.denominator + self.denominator * other.numerator
            self.reduce()
            return f'{self.com_numenator}/{self.com_denominator}'

    def __sub__(self, other):
        self.com_denominator = self.denominator * other.denominator
        self.com_numenator = self.numerator * other.denominator - self.denominator * other.numerator
        self.reduce()
        return f'{self.com_numenator}/{self.com_denominator}'

    def __mul__(self, other):
        self.com_denominator = self.denominator * other.denominator
        self.com_numenator = self.numerator * other.numerator
        self.reduce()
        return f'{self.com_numenator}/{self.com_denominator}'

    def __truediv__(self, other):
        self.com_denominator = self.denominator * other.numerator
        self.com_numenator = self.numerator * other.denominator
        self.reduce()
        return f'{self.com_numenator}/{self.com_denominator}'

    def reduce(self):
        for nod in range(max(self.com_denominator, self.com_numenator), 0, -1):
            if self.com_denominator % nod == 0 and self.com_numenator % nod == 0:
                self.com_denominator //= nod
                self.com_numenator //= nod
                return f'{self.com_numenator}/{self.com_denominator}'

