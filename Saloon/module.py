class Master:
    id = 1
    def __init__(self, name, phone):
        self.id = f'm{Master.id}'
        Master.id += 1
        self.name = name
        self.phone = phone
    
    def get_info(self):
        return f'{self.id} {self.name}'
    
class MastersList:
    def __init__(self):
        self.list = []
    
    def add_master(self, obj_master):
        self.list.append(obj_master)
    
    def delete_master(self,id_master):
        for master in self.list:
            if id_master == master.id:
                self.list.pop(self.list.index(master))
                # TODO вызов функции удаления мастрера из БД
                del master
# TEST
#master1 = Master('Katy', '43566')
#master2 = Master('Mo','4535644')
#master_list = MastersList()
#master_list.add_master(master1)
#master_list.add_master(master2)
#print(master_list.__dict__)
#master_list.delete_master(master1.id)
#print(master_list.__dict__)

class Client:
    id = 1
    def __init__(self, name, phone, discount) -> None:
        self.id = Client.id
        Client.id += 1
        self.name = name
        self.phone = phone
        self.discount = discount
    
    def get_info(self):
        return f'{self.name}'
    
class ClientsList:
    def __init__(self):
        self.list = []
    def add_client(self, obj_client):
        self.list.append(obj_client)
    
class Product:
    id = 1
    def __init__(self,name) -> None:
        self.id = f'p{Product.id}'
        Product.id += 1
        self.name = name
    
    def get_info(self):
        return f'{self.id} {self.name}'

class ProductsList:
    def __init__(self):
        self.list = []
    def add_product(self, obj_product):
        self.list.append(obj_product)
    
    def delete_product(self, id_product):
        for product in self.list:
            if id_product == product.id:
                self.list.pop(self.list.index(product))
                # TODO добавить функцию удаления продукта из БД
    
class Service:
    def __init__(self, date, product, client, master, price) -> None:
        self.date = date
        self.product = product
        self.client = client
        self.master = master
        self.price = price
        self.amount = price - client.discount * price
        self.salary = self.amount / 2
        self. profit = self.salary
    
    def get_info(self):
        return f'{self.__dict__}'
    
class ServicesList:
    def __init__(self) -> None:
        self.list = []
    def add_service(self,service):
        self.list.append(service)
    
    def delete_product(self, id_product):
        for product in self.list:
            # TODO ПРОПИСАТЬ УДАЛЕНИЯ СЕРВИСА 