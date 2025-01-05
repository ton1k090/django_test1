from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .forms import CommentForm
from blog.models import Post, Comment




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

    def get_context_data(self, **kwargs):
        '''Метод для вывода определенного контекста в шаблон'''
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm() # Использовать данную форму
        return context


class CreateComment(CreateView):
    '''Класс для отправки комментария и записи в бд'''
    model = Comment # Использовать данную модель
    form_class = CommentForm # Использовать данную форму

    def form_valid(self, form):
        '''Проверка формы на валидность и сохранение в бд'''
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save() # Сохранить форму
        return super().form_valid(form)

    def get_success_url(self):
        '''Формирование ссылки для перехода
        после отправки формы'''
        return self.object.post.get_absolute_url() # Забираем метод у модели постов

