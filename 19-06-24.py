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
class CountryCapital:
    def __init__(self):
        self.coun_cap={}
    def app(self,country,capital):
        self.coun_cap[country] = capital
        return self.coun_cap
    def desplay(self) -> str:
        return self.coun_cap
    def __str__(self) -> str:
        line_print = ''
        for i in self.coun_cap.items():
            line_print += ': '.join(i) + ' '
        return line_print
    def del_country(self,country):
        del self.coun_cap[country]


euro = CountryCapital()
euro.app('Россия', "Москва")
euro.app('КНР', "Пекин")
print(euro.desplay())
print(euro)
euro.del_country('КНР')
print(euro)
