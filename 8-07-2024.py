# Pattern SOLID (паттерн архитектуры классов)
## S (Принцип единственной ответственности. У класса должна быть только одна причина для изменения )
class TelephoneList:
    def __init__(self):
        self.telephone_list = {}
    
    def add_abonent(self, name, number):
        self.telephone_list[name] = number
    def desplay_abonent(self):
        for abonent in self.telephone_list.items():
            print(abonent)

class SaverToFile:
    def save_to_file(self, object, path):
        with open('','w') as f:
            f.write('')



t_list = TelephoneList()
t_list.add_abonent('Max', 89423674367834)
t_list.add_abonent('Anna', 8942369997834)
t_list.desplay_abonent()
## O (Открытости и закрытости: cущности должны быть открыты для расширений, но закрыты для изменений)
class DiscontCalculator:
    def __init__(self, season, price):
        self.season = season
        self.discont_price = price

    def get_price(self):
        return self.discont_price

class DiscontSummerCalculator(DiscontCalculator):
    def __init__(self, season, price):
        super().__init__(season, price)

    def get_price(self):
        return self.discont_price * 0.9

class DiscontWinterCalculator(DiscontCalculator):
    def __init__(self, season, price):
        super().__init__(season, price)

    def get_price(self):
        return self.discont_price * 0.75

calculator = DiscontSummerCalculator('summer', 220)
calculator2 = DiscontWinterCalculator('winter', 220)    
print(calculator.get_price(), calculator2.get_price())

## L (Принцип подстановки Барбары Лисков. Объекты классов должны быть легко заменяемы их экземплярами) 
class Car:
    def __init__(self, type):
        self.type = type
        self.property = {}

    def set_property(self, color, engine):
        self.property['color'] = color
        self.property['engine'] = engine
        return self.property

car1 = Car('SEDAN')
car1.set_property('red','electro')
car2 = Car('SEDAN')
car2.set_property('red','DVS')
cars = [car1, car2]
for car in cars:
    if car.property['color'] == 'red':
        print(car, 'Yes')

# I (Принцип разделения интерфейсов. Ни один экземпляр не должен зависеть от методов, которые он не использует)
class Telephone:
    pass


class Call:
    def call(self, obj):
         print('Возможность отправить смс')
class Sms:
    def sms(self, obj):
         print('Возможность отправить смс')

class AppleMobile(Telephone):
    def call(self):
        return super().call()
    def sms(self):
        return super().sms()

class XiomiMobile(Telephone):
    def call(self):
        return super().call()
    def sms(self):
        return super().sms()

class LandPhone(Telephone):
    def call(self):
        return super().call()

iphone15 = Telephone()

# D (Принцип инверсии зависимостей. Сущности более высокого уровня не зависят от сущностей низжего. 
# Всё зависит от абстракции. Абстракция не зависит от реализации, реализация зависит от абстракции)

class Player:
    def __init__(self, name, team):
        self.name = name
        self.team = team

class PlayerBase:
    def __init__(self):
        self.player_base = []

    def add_player(self, player):
        self.player_base.append(player)
        return self.player_base
    
    def get_player_of_team(self):
        for player in self.player_base:
            if player.team == 'GREEN':
                yield player

class Analiser:
    def __init__(self, list_player):
        for player in list_player.get_player_of_team():
            print(player.name)

obj1 = PlayerBase()
player1 = Player('Jo', 'RED')
player2 = Player('Max','GREEN')
player3 = Player('Leo', 'GREEN')
obj1.add_player(player1)
obj1.add_player(player3)
print(obj1.add_player(player2))
analisator = Analiser(obj1)

#task1
#создать фабрику пицц
#создать субкласс гавайская(топпинг: ананас, оливка, лук), пипперони(колбаса,  оливка, лук) и по своему рецепту(основа, вкус, топпинг)
#создание заказа класс
# закпись заказа txt
#
class PizzaFabric:
	def __init__(self, size, *topping):
  	self.size = size
    self.topping = list(*topping)
    
  def get_price(self):
  	return self.size * 30 + len(self.topping) * 20
    
class PizzaHawaii(PizzaFabric):
	def __init__(self, size, *topping):
  self.name = 'hawaii'
  	super().__init__(self, size, *topping)
    
  def get_price(self):
  	super().get_price(self)
    
class PizzaPepperoni(PizzaFabric):
	def __init__(self,size,*topping):
  	self.name = 'pepperoni'
  	super().__init__(self,size,*topping)
    
  def get_price(self):
  	super().get_price(self)
    
class PizzaCrafter(PizzaFabric):
	def __init__(self,size,*topping, name):
		self.name = name
  	super().__init__(self,size,*topping)
    self.nime=
  def get_price(self):
  	super().get_price(self)
    
class Basket:
  def __init__(self):
  	self.basket=[]
    
  def add_item(self,item):
  	self.basket.append(item)
    
  def delete_item(self,item):
  	if item in self.basket: 
       
