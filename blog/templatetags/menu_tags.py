from django import template
from blog.models import Category, Post

register = template.Library()


def get_all_categories():
    return Category.objects.all()


@register.simple_tag()
def get_list_category():
    """Вывод всех категорий"""
    return get_all_categories()


@register.inclusion_tag('blog/include/tags/top_menu.html')
def get_categories():
    '''Темплейт тег для отображения всех категорий'''
    category = Category.objects.all()
    return {'list_category': category}


@register.inclusion_tag('blog/include/tags/recipes_tag.html')
def get_last_posts():
    '''Темплейт тег для отображения последних 5 постов'''
    posts = Post.objects.select_related('category').order_by('-id')[:5]
    return {'list_last_post': posts }