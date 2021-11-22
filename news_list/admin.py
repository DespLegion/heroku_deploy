from django.contrib import admin

from .models import Category, Comment, News


class NewsShow(admin.ModelAdmin):
    list_display = ('id', 'sh_name', 'category', 'post_date')
    list_display_links = ('sh_name',)
    list_filter = ('category', 'post_date')
    search_fields = ('sh_name', 'post_date')

    # ////////////////////////////////////////////////////////////////////////
    # Отображение изображения в админке
    # Для отображения раскоментировать функцию и в list_display добавить
    # вызов функции 'show_img' в необходимый list_display
    # для работы необходимо еще импортировать from django.utils.safestring import mark_safe
    #
    # def show_img(self, obj):
    #     return mark_safe(f'<img src={obj.img.url} width="50" height="60">')
    # show_img.short_description = 'Изображение'
    # ////////////////////////////////////////////////////////////////////////


# Register your models here.
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(News, NewsShow)
