from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


class RecipeInline(admin.StackedInline):
    model = models.Recipe
    extra = 1


@admin.register(models.Post) # добавление модели в админку при помощи декоратора
class PostAdmin(admin.ModelAdmin):
    '''Добавляем модель постов в админку'''
    list_display = ('title', 'author', 'category', 'created_at', 'id') # поля для отображения в админке
    inlines = [RecipeInline]
    save_as = True
    save_on_top = True # кнопка сохранить сверху


@admin.register(models.Recipe)
class RecipyAdmin(admin.ModelAdmin):
    '''Добавляем модель рецептов в админку'''
    list_display = ('name', 'prep_time', 'cook_time', 'post') # поля для отображения в админке


'''Добавление других моделей в админку'''

admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment)

