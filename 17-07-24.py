#Многопоточность

import threading
#def f(name=None):
#    a = 0
#    while a < 10:
#        a += 1
#        print(f'{name} - {a}')
#print(threading.active_count())
#t1 = threading.Thread(name='Первый поток', target=f, kwargs={'name':'First'})
#t2 = threading.Thread(name='Второй поток', target=f, kwargs={'name':'Second'})
#t2.start()
#t1.start()
#print(threading.active_count(), threading.enumerate())
#t2.join()
#print('Поток Second завершен')
#task
#def f(list=[], mode='max'):
#    print(threading.active_count(), threading.enumerate())
#    if mode == 'max':
#        print(f'Максимальный элемент последовательности {max(list)}')
#    else:
#        print(f'Минимальный элемент последовательности {min(list)}')
#
#list = []
#a = input('Введите число')
#while a != '':
#    list.append(a)
#    a = input("Введите число")
#t1 = threading.Thread(name='Поток поиска максимального элемента', target=f, kwargs={'list': list, 'mode': 'max'})
#t2 = threading.Thread(name='Поток поиска минимального элемента', target=f, kwargs={'list': list, 'mode': 'min'})
#t1.start()
#t2.start()
#task2
#import threading
#list =[]
#while True:
#    try:
#       i = int( input('введите число'))
#       list.append(i)
#    except:
#       break
#
#def summ(*list):
#    print(f'Сумма элементов списка: {sum(list)}')
#
#def aver(*list):
#    print(f'Среднеарифметическое число элементов списка: {sum(list) // len(list)}')
#
#thread_sum = threading.Thread(name = 'Поиск суммы чисел',target= summ, args=list)
#thread_aver = threading.Thread(name = 'Поиск среднеарифметического числа', target = aver, args=list)
#thread_sum.start()
#thread_aver.start()
#task 3
#import threading
#path = 'C:/Users/3/Python31/Digits.txt'
#def odd(path):
#    odd_list = []
#    with open(path, 'r') as file:
#        for i in file:
#            if int(i) % 2 != 0:
#                odd_list.append(int(i))
#    with open('C:/Users/3/Python31/odd.txt', 'w') as file:
#        for i in odd_list:
#            file.write(f'{i}\n')
#      
#def write_even(path):
#    with open(path, 'r') as f:
#        try:
#            numbers = [int(n) for n in f.read().split()]
#        except:
#            print ('ошибка ')
#            return None
#    even_numbers = [str(n) for n in numbers if n % 2 == 0]
#    with open('C:/Users/3/Python31/even.txt', 'w') as f:
#        f.write('\n'.join(even_numbers))
#        
#thread_write_odd = threading.Thread(name='Добавление нечетных чисел в файл', target=odd, args= (path,))
#thread_write_even =threading.Thread(name='четные числа',target =write_even,args =(path,))
#thread_write_odd.start()
#thread_write_even.start()

import threading
path = 'C:/Users/3/Python31/Digits.txt'
search_word = input('Введите слово для поиска')

def search_f(path, search_word):
	with open(path, 'r') as file:
		text = file.read()
	if search_word in text:
		print(f'слово {search_word} есть в тексте')
	else:
		print('Такого слова нет')
      
thread_search_w1 = threading.Thread(name='Поиск слова', target=search_f, args=(path, search_word))
thread_search_w2 = threading.Thread(name='ее' , target=search_f, args=(path, 'name'))

thread_search_w1.start()
thread_search_w2.start()