import module as m
master_list = m.MastersList()
clients_list = m.ClientsList()
service_list = m.ServicesList()

while True:
    print(master_list.__dict__, clients_list.__dict__, service_list.__dict__, sep='\n')
    choice = input('1 - Мастера \n2 - Клиенты \n3 - Добавление записи \n4 - Удаление записи \n5 - Вывод записей \n0 - Выход\n')
   

    if choice == '1':
        choice = input('1 - Список мастеров \n2 - Добавить \n3 - Удалить \n0 - Выход\n')
        if choice == '1':
            pass

        elif choice == '2':
            name_master = input('Введите имя:')
            phone_master = input('Введите номер телефона:')
            master = m.Master(name_master, phone_master)
            # TODO добавить  мастера в bd
            master_list.add_master(master)

        elif choice == '3':
            id = input('Введите id:')
            master_list.delete_master(id)

        elif choice == '0':
            continue

        else:
            print('Неправильная команда')

    elif choice == '2':
           choice = input('1 - Список клиентов \n2 - Добавить клиента \n0 - Выход\n')
           if choice == '1':
                pass
           
           elif choice == '2':
                name_client = input('Введите имя:')
                phone_client = input('Введите номер:')
                discount_client = int(input('Введите размер скидки:'))
                client = m.Client(name_client, phone_client, discount_client / 100)
                clients_list.add_client(client)
                
           elif choice == '0':
                continue
           
           else:
                print('Неправильная команда')

        
    elif choice == '3':
         date = input('Введите дату:')
         product = input('Введите услугу:')
         for i in m.product_list.list:
                if product == i.name:
                     product = i
        # TODO ВЫВЕСТИ СПИСОК УСЛУГ
         client = int(input('Введите id клиента:'))
        #  TODO вывести список клиентов
         for i in clients_list.list:
                if client == i.id:
                     client = i
         master = input('Введите id мастера:')
        #  TODO вывести список мастеров из bd
         for i in master_list.list:
                if master == i.id:
                     master = i
         price = int(input('Введите цену:'))
         service = m.Service(date, product, client, master, price)
         service_list.add_service(service)
        #  TODO записать в bd


    elif choice == '4':
         id_service = int(input('Введите id:'))
         service_list.delete_service(id_service)
        #  TODO УДАЛИТЬ ЗАПИСЬ В BD

    elif choice == '5':
         pass
    
    elif choice == '0':
         break

            

            
