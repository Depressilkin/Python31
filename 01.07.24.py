# Паттерны проектирования
##Singletone (Одиночка)
#class Singletone:
#    _example = None # переменная - контроль наличия экземпляра класса
#    def __new__(clss):
#        if clss._example is None: # если экземпляра класса нет
#            clss._example = super(Singletone,clss).__new__(clss)# то создать
#        else:
#            print('Экземпляр класса уже существует') # иначе сообщить, что он уже существует
#        return clss._example
#
#class NotSingle:
#    pass
#
#obj1 = Singletone()
#print(obj1)
#obj2 = Singletone()
#print(obj2)
#print(obj1 is obj2)
#obj1 = NotSingle()
#obj2 = NotSingle()
#print(obj1 is obj2)
#print(obj2.__dict__)
#print(obj1)
#
##Factory
#class FactoryPizza:
#    def __init__(self, name, price):
#        self.name = name
#        self.price = price
#        print(f'Заказано: пицца {self.name}, цена {self.price} руб.')
#
#class Margarita(FactoryPizza):
#    def __init__(self):
#        self.name = 'Margarita'
#        self.price = 879
#        super().__init__(self.name, self.price)
#    def get_price(self):
#        return self.price
#    
#class Hawaii(FactoryPizza):
#    def __init__(self):
#        self.name = 'Hawaii'
#        self.price = 980
#        super().__init__(self.name, self.price)
#    def get_price(self):
#        return self.price
#    
#obj1 = Margarita()
#print(obj1.__dict__)
#obj2 = Hawaii()
#print(obj1.get_price())

##Abstract Factory
#from abc import ABC, abstractmethod
#class AbstractFactory(ABC):
#    @abstractmethod
#    def create_factory(self,name):
#        self.name = name
#        if self.name == 'Airbus':
#            return 'Создана фабрика Airbus'
#        else:
#            return 'Создана фабрика Boing'
#class AirbusFactory(AbstractFactory):
#    def create_factory(self, name):
#        return super().create_factory(name)
#    def create_airplane(self):
#        return AirbusAirplane()
#    def create_engine(self):
#        return AirbusEngine()
#
#class BoingFactory(AbstractFactory):
#    def create_factory(self, name):
#        return super().create_factory(name)
#    def create_airplane(self):
#        return BoingAirplane()
#    def create_engine(self):
#        return BoingEngine()    
#
#class AbstractAirplane(ABC):
#    pass
#class AirbusAirplane(AbstractAirplane):
#    def get_airplane(self):
#        return f'Создан самолет компании Airbus'
#    
#class BoingAirplane(AbstractAirplane):
#    def get_airplane(self):
#        return f'Создан самолет компании Boing'
#
#class AbstractEngine(ABC):
#    pass
#class AirbusEngine(AbstractEngine):
#    def get_engine(self):
#        return f'Создан двигатель компании Airbus'
#    
#class BoingEngine(AbstractEngine):
#    def get_engine(self):
#        return f'Создан двигатель компании Boing'
#    
#fabr1 = AirbusFactory()
#airpl1 = fabr1.create_airplane()
#print(airpl1)
#obj = AbstractFactory()
#print(obj)
#task3
import logging
logging.basicConfig(level='INFO', format='%(asctime)s - %(message)s')
class Digits:
  def __init__(self,path,*num):
    self.num = num
    with open(path, "w") as file:
      for i in num:
        file.write(f'{i}\n')
      file.write(f'Minimize: {min(num)}\n Maximize: {max(num)}')
    logger.logging_init(self)
  def get_dit(self):
    for i in self.num:
      print(i)
    logger.logging_dit(self)
  
  def get_max(self):
    print(max(self.num))
    logger.logging_max(self)
  def get_min(self):
    print(min(self.num))
    logger.logging_min(self)
class Logger:
  _instance = None
  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(Logger, cls).__new__(cls)
    return cls._instance
  
  def logging_init(self,other):
    logging.info(f'Выполнен метод записи в файл объекта {other}')
  def logging_dit(self,other):
    logging.info(f'Выполнен метод вывода чисел объекта {other}')

  def logging_max(self,other):
    logging.info(f'Выполнен метод поиска максимального объекта {other}')

  def logging_min(self,other):
    logging.info(f'Выполнен метод поиска минимального объекта {other}')

  def logging_to_file(self):
    pass
logger = Logger()
digits = Digits('C:/Users/3/Python31/Digits.txt',23,43,56,786,98,67,34,26,38,16)
#print(digits.num)
digits.get_dit()
digits.get_max()
digits.get_min()
digits2 = Digits('C:/Users/3/Python31/Digits.txt',23,43,56,786,26,38,16)
#obj = Logger()
#print(obj)
#filename='myapp.log'
#import logging
##filename='myapp.log',
#logging.basicConfig(filename='myapp.log', level='INFO', format='%(asctime)s - %(message)s')
#def _summ(x,y):
#    result = x + y
#    logging.info(f'Выполнена функция _summ с параметрами(х={x}, y={y}). Результат = {result}')
#    return result
#x = 2
#y = 6
#logging.info(f'введены переменные(х={x}, y={y})')
#_summ(x,y)
#
#def logger(func):
#    func()
#    logging.info(f'Выполнена функция {func}. Результат = {func()}')
#
#def hello():
#    return 'Hello'
#logger(hello)