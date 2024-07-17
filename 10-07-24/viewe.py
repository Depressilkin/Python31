class Viewer:
    def __init__(self):
        pass

    def viewe(self, article):
        return f'Название статьи:{article.title}\n{article.previewe}...Читать далее.\nАвтор:{article.creater}'

    def get_text(self, article):
        return f'{article.text}'

    def get_list_article(self,list):
        post = ''
        number_art = 0
        for art in list:
            number_art += 1
            post += f' {number_art} {art.title}\n'
        return post