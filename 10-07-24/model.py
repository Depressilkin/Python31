class Article:
    def __init__(self, title, previewe, text, creater, source):
        self.title = title
        self.previewe = previewe
        self.text = text
        self.creater = creater
        self.source = source
with open('C:/Users/3/Python31/10-07-24/Article.txt', 'r') as file:
    title = file.readline()
    previewe = file.readline()
    text = file.readline()
    creater = file.readline()
    source = file.readline()

article = Article(title, previewe, text, creater, source)
article2 = Article('Евро 2024', 'Краткое содержание', "Здесь текст", "Автор", "Источник")