from model import article, article2
from viewe import Viewer
list = [article2, article]
viewer = Viewer()
print(viewer.get_list_article(list))
print('Нажмите номер стaтьи для просмотра')
user_token = int(input())
article = list[user_token - 1]
print(viewer.viewe(article))
print('Нажмите 1 для просмотра полного содержания')
user_token = input()
if user_token == '1':
    print(viewer.get_text(article))