from os import strerror
try:
    with open('C:/Users/3/Python31/130524/Content.txt') as file:
        text = file.read()
except IOError as err:
    print(f'Файл не удалось открыть! {strerror(err.errno)}')
print(text)
word_f = input('Введите слово, которое нужно заменить')
word_c = input('Введите слово, на которое нужно заменить')
text = text.replace(word_f, word_c)
print(text)