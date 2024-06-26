# task 3
#class User:
#    def __init__(self, user_login, user_password, next_user= None):
#        self.user_login = user_login
#        self.user_password = user_password
#        self.next_user = next_user
#class BaseData:
#    head = None
#    lenght = 0
#    def append(self, user_login, user_password):
#        user = self.head
#        if self.head == None:
#            self.head = User(user_login, user_password)
#        else:
#            while user.next_user != None:
#                user = user.next_user
#            user.next_user = User(user_login, user_password)
#        self.lenght += 1
#    def __str__(self):
#        user = self.head
#        desplay = '['
#        while user.next_user != None:
#            desplay += user.user_login +', '
#            user = user.next_user
#        desplay +=  user.user_login + ']'
#        return desplay
#    def del_user(self,user_login):
#        user = self.head
#        ex_user = None
#        if user.user_login == self.head.user_login and user.user_login == user_login:
#            self.head = user.next_user
#            del user
#        else:
#            while user.user_login != user_login:
#                ex_user = user
#                user = user.next_user
#            ex_user.next_user = user.next_user
#            del user
#        self.lenght -= 1
#    def found(self, user_login):
#        user = self.head
#        while user.next_user != None:
#            if user.user_login == user_login:
#                return print('Есть такой пользователь')
#            user = user.next_user
#        if user.user_login == user_login:
#            return print('Есть такой пользователь')
#        else:
#            print('Такого пользователя нет')
#    def sub_login(self, old_login, new_login):
#        user = self.head
#        while user.user_login != old_login:
#            user = user.next_user
#        user.user_login = new_login
#def start():
#    bd = BaseData()
#    while True:
#        print('Меню:\n1 - добавить пользователя\n2 - удалить пользователя\n3 - поиск пользователя\n4 - заменить логин\n5 - вывод всей БД\n6 - выход из программы')
#        change = input('Выберите команду')
#        if change == '1':
#            print('Дабавление пользователя')
#            login = input('Введите логин для добавления')
#            password = input('Введите пароль для добавления')
#            bd.append(login,password)
#        elif change == '2':
#             print('Удаление пользователя')
#             login = input('Введите логин для удаления')
#             bd.del_user(login)
#        elif change == '3':
#            print('Поиск пользователя')
#            login = input('Введите логин для поиска')
#            bd.found(login)
#        elif change == '4':
#            print('Замена логина')
#            old_login = input('Введите старый логин для замены')
#            new_login = input('Введите новый логин для замены')
#            bd.sub_login(old_login,new_login)
#        elif change == '5':
#            print(bd)
#        elif change == '6':
#            break
#        else:
#            print('Нет такой команды')
#    print("Завершение работы")
#start()

#Упаковка и распаковка (операторы * и **)
## Упаковка
#var1 = 9
#var2 = 're'
#var3 = True
#*list ,= var1, var2, var3
#print(list)
#def f(*param):
#    print(param[1:3])
#f(1,2,3,4,5)
#def f2(param1=1,**param):
#    print(param1,param)
#f2(param2=2,param3=3)
### Распаковка
#var4 , var5 = [4,5]
#print(var4 , var5)
##
#var4 , *var5 = [4,5, 5, 6]
#print(var4 , var5)
##
#*var4 , var5 = [4,5, 5, 6]
#print(var4 , var5)
##
#*var4 , var5 = [ 6]
#print(var4 , var5)
## распаковка в цикле
#data = [
#    ['Max', 'Max'],
#    ['Min', 'Min']
#]
#for i, j in data:
#    print(i,j)
#var6 = -5, 5
#print(var6)
## распаковка итерируемых объектов
#for i in range(*var6):
#    print(i)
#
#print(*range(*var6))
## распаковка словаря
#a = {0:'0', 1:'1'}
#b = {2:'2', 3:'3'}
#c = a | b
#d = {**a, **b}
#print(c, d)
#task 1
#class CountryCapital:
#    def __init__(self):
#        self.coun_cap={}
#    def app_or_change(self,country,capital):
#        self.coun_cap[country] = capital
#        return self.coun_cap
#    def desplay(self) -> str:
#        return self.coun_cap
#    def __str__(self) -> str:
#        line_print = ''
#        for i in self.coun_cap.items():
#            line_print += ': '.join(i) + ' '
#        return line_print
#    def del_country(self,country):
#        del self.coun_cap[country]
#    
#    def found_country(self, country):
#        if country in self.coun_cap.keys():
#            return True
#        else:
#            return False
#    
#    def found_capital(self, country):
#        if country in self.coun_cap.values():
#            return True
#        else:
#            return False
#    
#    def app_massiv(self, *country_capital):
#        for index in range(0,len(country_capital),2):
#            self.coun_cap[country_capital[index]] = country_capital[index + 1]
#        return self.coun_cap
#
## C:\Users\3\Python31\19-06-24.py
#    def save_as_text(self, path, file_name):
#        with open(f'{path}/{file_name}','w') as f:
#            base_date = f
#            print(self.coun_cap.items()) 
#            for item in self.coun_cap.items():
#                item = ' - '.join(item)
#                base_date.write(item+'\n')
#
#euro = CountryCapital()
#euro.app_or_change('Россия', "Москва")
#euro.app_or_change('КНР', "Пекин")
#print(euro.desplay())
#print(euro)
#euro.del_country('КНР')
#print(euro)
#print(euro.found_country('Россия'))
#print(euro.found_capital('Москва'))
#print(euro.app_massiv('England', 'London', 'France', 'Paris', 'Германия', 'Берлин'))
#euro.save_as_text('C:/Users/3/Python31', 'CountryCapital.txt')
#TASK 2
class Songs:
  def __init__(self):
    self.songsTable = {}
    
  def add_autor(self, autor, *album):
    self.songsTable[autor] = [*album]
    return self.songsTable
    
  def add_album(self, album, autor):
    self.songsTable[autor].append(album)
    return self.songsTable
  def del_autor(self, autor):
    if autor in self.songsTable:
      del self.songsTable[autor]
      return self.songsTable
    else:
      return 'Автор не найден'
    
  def del_album(self, autor, album):
    if autor in self.songsTable:
      self.songsTable[autor].remove(album)
      return self.songsTable
    else:
      print('Автор не найден')
  def change_album(self, autor, old_album, new_album):
    if old_album in self.songsTable[autor]:
      self.songsTable[autor][self.songsTable[autor].index(old_album)] = new_album
      return self.songsTable
        #альтернативно
        #self.songsTable[autor][self.songaTable[autor].index(old_album)] = new_albom
    else:
      return 'Альбом не найден'
    
  def add_array_album(self, autor,*album):
    if autor in self.songsTable:
      for item in album:
        self.songsTable[autor].append(item)
      return self.songsTable
    else:
      return 'Автор не найден'
  
  def save_file(self, path):
    with open(path, 'w') as file:
      for item in self.songsTable.items():
        file.write(item[0] + ' ' + str(item[1])[1:-1] + '\n')
  
  def load_file(self, path):
    with open(path, 'r') as file:
      for item in file :
        index_autor = item.find("'")
        autor = item [0:index_autor-1]
        item =item.replace("'","")
        list_album =list(item[index_autor:].split(', '))
        self.songsTable[autor] = list_album
        self.songsTable[autor][-1] = self.songsTable[autor][-1][:-1]
    return self.songsTable

#C:/Users/3/Python31/MusicBase.txt    
#obj1 = Songs()
#obj1.add_autor('Автор1','Первый', 'Второй')
#print(obj1.__dict__)
#print(obj1.add_album('Alb3','Автор1'))
#obj1.add_autor('Автор2','Первый', 'Второй')
#print(obj1.del_album('Автор1','Второй'))
#print(obj1.change_album('Автор1', 'Alb3', 'Alb5'))
#print(obj1.add_array_album('Автор1','5','seven','8'))
#obj1.save_file('C:/Users/3/Python31/MusicBase.txt')
#obj2 = Songs()
#print(obj2.load_file('C:/Users/3/Python31/MusicBase.txt '))