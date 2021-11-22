from datetime import date

from django.db import models


# Create your models here.
class Category(models.Model):
    """Категории новостей"""
    name = models.CharField('Категория новостей', max_length=150)
    description = models.TextField('Описание категории')
    cat_img = models.ImageField('Изображение для категории', upload_to='news_list/media/img/news/cat/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория новостей'
        verbose_name_plural = 'Категории новостей'


class News(models.Model):
    """Новость"""
    sh_name = models.CharField('Краткий заголовок новости', max_length=50)
    name = models.CharField('Заголовок новости', max_length=150)
    img = models.ImageField('Изображение новости', upload_to='news_list/media/img/news/')
    body = models.TextField('Текст новости')
    post_date = models.DateField('Дата публикации', default=date.today)
    category = models.ForeignKey(Category, verbose_name = 'Категория', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.sh_name

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comment(models.Model):
    """Коментарий к новости"""
    user = models.CharField('Имя пользователя, оставившего комментарий', max_length=100)
    comment_text = models.TextField('Текст коментария', max_length=500)
    comm_post_date = models.DateField('Дата публикации комментария', default=date.today)
    news = models.ForeignKey('News', verbose_name='Новость', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
