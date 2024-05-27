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

    def substraction(self):
        a = int(input('Введите числитель второго слагаемого'))
        b = int(input('Введите знаменатель второго слагаемого'))
        self.com_denominator = self.denominator * b
        self.com_numenator = self.numerator * b - a * self.denominator
        self.reduce()

    def multiplication(self):
        c = int(input('Введите числитель второго множителя'))
        d = int(input('Введите знаменатель второго множителя'))
        self.com_denominator = self.denominator * d
        self.com_numenator = self.numerator * c
        self.reduce()

    def division(self):
        c = int(input('Введите числитель делителя'))
        d = int(input('Введите знаменатель делителя'))
        self.com_denominator = self.denominator * c
        self.com_numenator = self.numerator * d
        self.reduce()

    def reduce(self):
        for nod in range(max(self.com_denominator, self.com_numenator), 0, -1):
            if self.com_denominator % nod == 0 and self.com_numenator % nod == 0:
                self.com_denominator //= nod
                self.com_numenator //= nod
                break
        self.numerator = self.com_numenator
        self.denominator = self.com_denominator
    @staticmethod
    def f_counter():
        print(f'Создано {Fraction.counter} экземпляров класса')
Fraction.f_counter()
obj = Fraction(23,34)
Fraction.f_counter()

