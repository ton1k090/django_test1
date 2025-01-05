from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    '''Класс для заполнения полей отправки комментария'''
    class Meta:
        model = Comment # Использовать данную модель
        exclude = ['created_at', 'post'] # Игнорировать данные поля
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email'}),
            'website': forms.TextInput(attrs={'placeholder': 'website'}),
            'message': forms.Textarea(attrs={'placeholder': 'message'})
        }
