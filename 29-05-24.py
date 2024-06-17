##task 4
#class Date:
#    month_voc = {'1':31, '2':28, '3':31, '4':30, '5':31, '6':30, '7':31, '8':31, '9':30, '10':31, '11':30, '12':31}
#    def __init__(self, d, m, y):
#        self.d = d
#        self.m = m
#        self.y = y
#        self.get_convert_date()
#    
#    def get_convert_month(self):
#        summ_day = 0
#        for month in range(1,self.m+1):
#            summ_day += Date.month_voc[str(month)]
#        return summ_day
#    def get_counter_leap_year(self):
#        cly = 0
#        for i in range(self.y+1):
#            if i % 4 == 0 or (i % 100 == 0 and i % 400 == 0):
#                cly += 1
#        return cly
#
#    def get_convert_year(self):
#        return (self.y * 365 + self.get_counter_leap_year())
#
#    def get_convert_date(self):
#        self.convert_date = self.get_convert_year() + self.get_convert_month() + self.d
#        return self.convert_date
#    
#    def __sub__(self,other):
#        if isinstance(other,Date):
#            return f'Разность дат: {self.convert_date - other.convert_date} д.'
#        else:
#            return f'Разность дат: {self.convert_date - other} д.'
#    
#    def get_inver_convert_date(self):
#        self.convert_month = 1
#        self.convert_year = (self.convert_date - self.get_counter_leap_year()) // 365 
#        self.convert_day = (self.convert_date - self.get_counter_leap_year()) % 365 - 31
#        print(self.convert_day)
#        while self.convert_day > Date.month_voc[str(self.convert_month)]:
#            self.convert_day -= Date.month_voc[str(self.convert_month)]
#            self.convert_month += 1
#        return f'{self.convert_day}.{self.convert_month}.{self.convert_year}'
#    
#    def __add__(self, other):
#        self.convert_date += other
#        return self.get_inver_convert_date()
#
#obj1 = Date(29,5,2024)
#print(obj1.__dict__)
#obj2 = Date(25, 5, 2024)
#print(obj1 - obj2)
#print(obj2 + 1)
#
#task 4
#class Employer:
#    def __init__(self, var):
#        self.var = var
#    def _print(self):
#        return f'Это {self.var}'
#class President(Employer):
#    def __init__(self, var):
#        super().__init__(var)
#    def _print(self):
#        return super()._print()
#class Manager(Employer):
#    def __init__(self, var):
#        super().__init__(var)
#        self.type = 'Manager'
#    def _print(+self):
#        return super()._print()
#    def get_type(self):
#        return f'{self.type}'
#
#
#obj1 = President('Президент')
#print(obj1._print())
#obj2 = Manager('Менеджер')
#print(obj2.get_type())
#task 3
#class Pet:
#    def __init__(self, sound, show):
#        self.sound = sound
#        self.show = show
#    def get_sound(self):
#        return f'{self.sound*2}'
#    def get_show (self):
#        return f'{self.show}'
#    def get_type(self,type):
#        return f'{type}'
#
#class Cat(Pet):
#    def __init__(self, sound, show):
#        super().__init__(sound, show)
#        self.type = 'Кот'
#    def get_sound(self):
#        return super().get_sound()
#    def get_show(self):
#        return super().get_show()
#    def get_type(self):
#        return super().get_type(self.type)
#    
#cat = Cat('muw-', 'Tom')
#print(cat.get_sound(), cat.get_type())
