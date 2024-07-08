##Pattern Strategy
#class User:
#    def __init__(self):
#        self.strategy = None
#    def set_strategy(self,strategy):
#        self.strategy = strategy
#class StrategyA:
#    def get_strategy():
#        return f'Стратегия Аренды' 
#class StrategyB:
#    def get_strategy():
#        return f'Стратегия Покупки'
#user = User()
#print(f'Меню:\n1 - аренда\n2 - покупка')
#change = input()
#if change == '1':
#    user.set_strategy(StrategyA.get_strategy())
#else:
#    user.set_strategy(StrategyB.get_strategy())
#print(user.strategy)
##Pattern Adapter
#class RuWallet:
#    def __init__(self,rub):
#        self.wallet = rub
#    def get_wallet(self):
#        return f'{self.wallet} руб'
#class KztWallet:
#    def __init__(self,tng):
#        self.wallet = tng
#    def get_wallet(self):
#        return f'{self.wallet} тенге'
#class AdapterKztWallet:
#    def __init__(self,rub):
#        self.wallet = rub * 5.38
#    def  get_wallet(self):
#        return f'{self.wallet} тенге'
#rub = 1
#tng = 5.38    
#walletA = RuWallet(rub)
#walletB = KztWallet(tng)
#walletVPN = AdapterKztWallet(RuWallet(rub).wallet)
#print(walletA.get_wallet(),walletB.get_wallet(),walletVPN.get_wallet())
## Pattern Fasade
#class FasadeStudio:
#    def __init__(self):
#        pass
#
#    def get_designe(self):
#        return Designer()
#    
#    def get_code(self):
#        return Coder()
#
#    def get_test(self):
#        return Tester()
#
#class Designer:
#    def __init__(self):
#        print('Работа отдела дизайнеров')
#class Coder:
#    def __init__(self):
#        print('Работа отдела программистов')
#class Tester:
#    def __init__(self):
#        print('Работа отдела тестировщиков')
#web_studio = FasadeStudio()
#print(web_studio)
#web_studio.get_designe()
#web_studio.get_code()
#web_studio.get_test()
## pattern Iterator
#class Market:
#    def __init__(self, product):
#        self.product = product
#        self.index = 0
#    
#    def __iter__(self):
#        return self
#
#    def __next__(self):
#        if self.index < len(self.product):
#            item = self.product[self.index]
#            self.index += 1
#            return item
#        else:
#            raise StopIteration
#product = ['айфон','самсунг','сяоми']        
#yandex_market = Market(product)
#for item in yandex_market:
#    print(item)
#task1
#
#class Digits:
#    def __init__(self):
#        self.num =None
#    def input_dig(self,strateg ):
#        c = strateg
#        self.num = c.num    		
#class ManualEntry:
#    def __init__(self,*num):
#        self.num=num    	
#class PathEntry:
#    def __init__(self,path):
#        self.num = []
#        with open(path,'r') as n:
#            for i in n:
#                self.num.append(int(i))
#a = Digits()
#a.input_dig(ManualEntry(2,21,53,44))
#print(a.num)
#a.input_dig(PathEntry('CountryCapital.txt'))
#print(a.num)
# task 4
## pattern Iterator
class Group:
    def __init__(self, students):
        self.students = students
        self.index = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.students):
            item = self.students[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

group = [
    {'Lee':[20, 4.5]},
    {'Leo':[20, 4.1]},
    {'Leon':[20, 5.0]}
]

ip3 = Group(group)
print(ip3.students)
