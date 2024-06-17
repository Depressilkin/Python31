## динамический массив
#s = [12, '34', 56, 567]
#print(s[2])
#s.append(3) # предпочтительный
#s.insert(0,'первый')
#s[2] = 34
#
##print(s)
##print(s[1:3])
#
## односвязный список
## task 1
#class LinkList:
#    head = None
#    lenght = 0
#    class Node:
#        def __init__(self, element, next_node = None):
#            self.element = element
#            self.next_node = next_node
#
#    def append(self, element): # метод добавления в конец массива
#        if self.head == None:
#            self.head = self.Node(element)
#        else:
#            node = self.head
#            while node.next_node != None:
#                node = node.next_node
#            node.next_node = self.Node(element)
#        self.lenght += 1
#        return element
#    def __str__(self): # метод вывода массива
#        node = self.head
#        line_list = '['
#        while node.next_node != None:
#            line_list += str(node.element) + ', '
#            node = node.next_node
#        line_list += str(node.element) + ']'
#        return line_list
#
#    def insert(self,index, element): # метод добавления элемента в массив по индексу
#        current_index = 0
#        node = self.head
#        prev_node = self.head
#        if index == 0:
#            self.head = self.Node(element, next_node=node)
#        else:
#            while index > current_index:
#                current_index += 1
#                prev_node = node
#                node = node.next_node
#            prev_node.next_node = self.Node(element, next_node=node)
#        self.lenght += 1
#        return element
#
#    def __delitem__(self, index): # метод удаления элемента по индексу
#        current_index = 0
#        node = self.head
#        prev_node = self.head
#        if index == 0:
#            self.head = node.next_node
#            del node
#        else:
#            while index > current_index:
#                current_index += 1
#                prev_node = node
#                node = node.next_node
#            prev_node.next_node = node.next_node
#            del node
#        self.lenght -= 1
#    
#    def found(self, element): # метод поиска элемента
#        node = self.head
#        for i in range(self.lenght):
#            if node.element == element:
#                return print('Есть такой элемент')
#            node = node.next_node
#        return print('Такого элемента нет')
#    
#    def change(self, index, element): # метод замены значения элемента по индексу
#        node = self.head
#        current_index = 0
#        while current_index != index:
#            node = node.next_node
#            current_index += 1
#        node.element = element
#        return element
#
#m = LinkList()
#m.append(2)
#m.append(4)
#m.append(9)
#m.append(12)
#m.append(16)
#m.insert(2,43)
#m.change(2, 34)
#print(m)
# task 2

#class DoubleLinkList:
#    head = None
#    tail = None
#    lenght = 0
#    class Node:
#        def __init__(self, element, next_node = None, prev_node = None):
#            self.element = element
#            self.next_node = next_node
#            self.prev_node = prev_node
#    
#    def append(self, element):
#        if self.head == None:
#            self.head = self.tail = self.Node(element)
#        else:
#            node = self.head
#            while node.next_node != None:
#                node = node.next_node
#            self.tail = self.Node(element, next_node = None, prev_node = node)
#            node.next_node = self.tail
#        self.lenght += 1
#        return element
#
#    def __str__(self):
#        node = self.head
#        line_list = '['
#        while node.next_node != None:
#            line_list += str(node.element) + ', '
#            node = node.next_node
#        line_list += str(node.element) + ']'
#        return line_list
#    def insert(self, index, element):
#        current_index = 0
#        node = self.head
#        prev_node = None
#        next_node = node.next_node
#        if index == 0:
#            self.head = self.Node(element, next_node= node )
#            node.prev_node = self.head
#        else:
#            while current_index != index:
#                current_index += 1
#                prev_node = node
#                node = next_node
#                next_node = node.next_node
#            node.prev_node =  prev_node.next_node = self.Node(element, next_node= node, prev_node= prev_node)
#        self.lenght += 1
#        return element
#    
#    def __delitem__(self, index):
#        current_index = 0
#        node = self.head
#        prev_node = None
#        next_node = node.next_node
#        if index == 0:
#            next_node.prev_node = None
#            self.head = next_node
#            del node
#        else:
#            while index != current_index:
#                current_index += 1
#                prev_node = node
#                node = node.next_node
#                next_node = node.next_node
#            prev_node.next_node = next_node
#            next_node.prev_node = prev_node
#            del node
#        self.lenght -= 1
#    def found(self, element):
#        node = self.head
#        for i in range(self.lenght):
#            if node.element == element:
#                return 'Такой элемент есть!'
#            node = node.next_node
#        return 'Такой элемент отсутствует!'
#    def change(self, index, new_element):
#        node = self.head
#        for i in range(self.lenght):
#            if i == index:
#                node.element = new_element
#            node = node.next_node
#        return new_element
#mass = DoubleLinkList()
#mass.append(2)
#mass.append(12)
#mass.append(22)
#mass.insert(0,3)
#mass.insert(2,5)
#del mass[0]
#del mass[2]
#print(mass.found(5), mass.found(13), sep='\n')
#mass.change(1,4)
#print(mass)

#task3
