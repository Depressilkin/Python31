# PICKLE AND JSON
## pickle dump(что выгрузить, куда выгрузить), load(откуда выгрузить)
#from pickle import dump, load
##
class MyClass:
    def __init__(self, attr):
        self.atr = attr
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
var1 = 'Python'
#var2 = 3142356
var3 = MyClass('Attr')
#var_list = [var3, var1]
#path = 'C:/Users/3/Python31/My_File.pkl'
#Выгрузка в файл
#with open(path,'wb') as file:
#    dump(var3, file)

#Загрузка из файла
#with open(path, 'rb') as file:
#    var4 = load(file)
#print(var4.__dict__)

## JSON dump(что выгрузить, куда выгрузить), load(откуда выгрузить)
import json
path = 'C:/Users/3/Python31/My_File.json'
var3.name = 'John'
#Выгрузка в файл
with open(path,'w') as file:
    json.dump(var3.toJson(),file)
#Загрузка из файла
with open(path, 'r') as file:
    var5 = json.load(file)
print(var5)
#task 1
#class Jet:
#    def __init__(self,name = None,type = None):
#        self.name = name
#        self.type = type
#    def get_attr(self):
#        return f'Название:{self.name}, тип:{self.type}'
#    def dump_as_file(self,path):
#        with open(path,'wb') as file:
#            dump(self,file)
#    def load_as_file(path):
#        with open(path,'rb') as file:
#            return load(file)
#            
#obj1 = Jet('Boeing','Passanger')
#obj2 =Jet('Airbus','Cargo')
#print(obj2.get_attr())
#obj1.dump_as_file('C:/Users/3/Python31/My_File.pkl')
#obj3 = Jet.load_as_file('C:/Users/3/Python31/My_File.pkl')
#print(obj3.__dict__)