#class FixSizeStack:
#    def __init__(self, size):
#        self.size = size
#        self.stack = []
#    def push(self, element):
#        if len(self.stack) < self.size:
#            self.stack.append(element)
#            return self.stack
#        else:
#            return 'Стэк заполнен'
#    def pop(self):
#        if len(self.stack) > 0:
#            self.stack.pop(-1)
#            return self.stack
#        return 'Стэк пуст'
#
#    def counter(self):
#        return f'Количество элементов в стэке {len(self.stack)}'
#    
#    def is_empty(self):
#        if len(self.stack) == 0:
#            return True
#        else:
#            return False
#
#    def is_full(self):
#        if len(self.stack) == self.size:
#            return True
#        else:
#            return False
#    def full_clear(self):
#        self.stack.clear()
#        return self.stack
#    
#    def peek(self):
#        return self.stack[-1]
#
#my_stack = FixSizeStack(5)
#print(my_stack.push(2))
#print(my_stack.push(4))
#print(my_stack.push(14))
#print(my_stack.push(2))
#print(my_stack.push(4))
#print(my_stack.push(14))
#print(my_stack.pop())
#print(my_stack.pop())
#print(my_stack.pop())
#print(my_stack.counter())
#print(my_stack.is_empty())
#stack2 = FixSizeStack(1)
#print(stack2.push(2))
#print(stack2.is_empty())
#print(my_stack.is_full())
#print(stack2.is_full())
#print(stack2.full_clear())
#print(my_stack.peek())

# task 4
#class Stack:
#    def __init__(self):
#        self.stack = []
#    def push(self, element):
#            self.stack.append(element)
#            return self.stack
#
#    def pop(self):
#        if len(self.stack) > 0:
#            self.stack.pop(-1)
#            return self.stack
#        return 'Стэк пуст'
#
#    def counter(self):
#        return f'Количество элементов в стэке {len(self.stack)}'
#    
#    def is_empty(self):
#        if len(self.stack) == 0:
#            return True
#        else:
#            return False
#
#    def full_clear(self):
#        self.stack.clear()
#        return self.stack
#    
#    def peek(self):
#        if self.stack:
#            return self.stack[-1]
#        else:
#            return 'Стэк пустой'

# task1
#class Queue:
#    def __init__(self):
#        self.queue = []
#    
#    def show(self):
#        return self.queue
#    
#    def enqueue(self, element):
#        self.queue.append(element)
#        return self.queue
#
#    def dequeue(self):
#        if len(self.queue) != 0:
#            self.queue.pop(0)
#            return self.queue
#        return 'Очередь пуста'
#    def isEmpty(self):
#        if self.queue:
#            return False
#        else:
#            return True
#    
#    def isFull(self):
#        return f'Количество элементов в очереди {len(self.queue)}'
#
#
#my_queue = Queue()
#my_queue.enqueue(2)
#my_queue.enqueue(3)
#my_queue.enqueue(4)
#my_queue.dequeue()
#print(my_queue.show())
#print(my_queue.isEmpty())
#print(my_queue.isFull())
#task 2
#class PriorityQueue:
#    def __init__(self):
#        self.queue = []
#    
#    def insert_with_priority(self, element, priority):
#        self.queue.append([element, priority])
#        self.queue.sort(reverse=True, key= lambda x: x[1])
#        return self.queue
#    
#    def show(self):
#        return self.queue
#    
#    def pull_hightes_priority_element(self):
#        if self.queue:
#            self.queue.pop(0)
#            return self.queue
#        else:
#            return 'Очередь пустая'
#    
#    def peek(self):
#        return self.queue[0]
#    
#my_prior_queue = PriorityQueue()
#my_prior_queue.insert_with_priority(1, 0.5)
#my_prior_queue.insert_with_priority(3, 0.7)
#my_prior_queue.insert_with_priority(4, 0.2)
#my_prior_queue.pull_hightes_priority_element()
#print(my_prior_queue.peek())
#print(my_prior_queue.show())
