#task 6
#from os import strerror
#try:
#    with open('C:/Users/3/Python31/130524/Content.txt') as file:
#        text = file.read()
#except IOError as err:
#    print(f'Файл не удалось открыть! {strerror(err.errno)}')
#print(text)
#word_f = input('Введите слово, которое нужно заменить')
#word_c = input('Введите слово, на которое нужно заменить')
#text = text.replace(word_f, word_c)
#print(text)
#try:
#    with open('C:/Users/3/Python31/130524/Content.txt','w') as file:
#        file.write(text)
#except IOError as err:
#    print(f'Файл не удалось открыть! {strerror(err.errno)}')
## task 5
#from os import strerror
#try:
#    with open('C:/Users/3/Python31/130524/Content.txt') as file:
#        text = file.read()
#except IOError as err:
#    print(f'Файл не удалось открыть! {strerror(err.errno)}')
#word_f = input('Введите слово, которое нужно подсчетать')
#print(text.count(word_f))

## task 4
from os import strerror
try:
    with open('C:/Users/3/Python31/130524/Content.txt') as file:
        max_l = 0
        for i in file:
            if len(i) > max_l:
                max_l = len(i)
        print(max_l)
except IOError as err:
    print(f'Файл не удалось открыть! {strerror(err.errno)}')

