from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post


class HomeView(ListView):
    '''Класс для вывода информации'''
    model = Post
    paginate_by = 9
    template_name = 'blog/home.html'


class PostListView(ListView):
    '''Класс для вывода постов из модели'''
    model = Post

    def get_queryset(self):
        '''Получить данные по определенным параметрам'''
        return Post.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')


class PostDetailView(DetailView):
    '''Класс для вывода поста из моделей'''
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'



