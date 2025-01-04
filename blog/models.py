from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User


class Category(MPTTModel):
    '''Модель категорий'''
    name = models.CharField(max_length=100) # Поле ввода текста с ограничением в 100 символов
    slug = models.SlugField(max_length=100) # Поле слаг для формирования ссылки
    parent = TreeForeignKey('self',
                            related_name='children',
                            on_delete=models.SET_NULL,
                            null=True,
                            blank=True
    )

    def __str__(self):
        return self.name


class MPTTMeta:
    '''Модель для создания вложенных категорий'''
    order_insertion_by = ['name']


class Tag(models.Model):
    '''Модель тегов'''
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    '''Модель постов'''
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='articles') # Поле для изображения
    text = models.TextField() # Поля текстового ввода без ограничений
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
    ) # Поле первичного ключа для привязки поля пост к категории
    tags = models.ManyToManyField(Tag, related_name='post') # Поле для множественной привязки многий ко многим
    created_at = models.DateTimeField(auto_now_add=True) # Поле даты с автозаполнением
    slug = models.SlugField(max_length=200, default='', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        '''Функция для формирования ссылки для каждого поста'''
        return reverse('post_single', kwargs={'slug': self.category.slug, 'post_slug': self.slug})

    def get_recipes(self):
        '''Функция получения всех рецептов'''
        return self.recipes.all()


class Recipe(models.Model):
    '''Модель рецептов'''
    name = models.CharField(max_length=100)
    serves = models.CharField(max_length=50)
    prep_time = models.PositiveIntegerField(default=0) # Поле положительного числа по умолчанию 0
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = RichTextField() # отформатированное поле ввода текста
    directions = RichTextField()
    post = models.ForeignKey(Post,
                            related_name='recipes',
                            on_delete=models.SET_NULL,
                            null=True,
                            blank=True
                            )


class Comment(models.Model):
    '''Модель комментариев'''
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100) # Поле для почты
    website = models.CharField(max_length=150)
    message = models.TextField(max_length=500)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)