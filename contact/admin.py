from django.contrib import admin
from .models import ContactModel, ContactLink, About, Social, ImageAbout


class ImageAboutInline(admin.StackedInline):
    '''Класс для добавления нескольких изображений в один пост модели About
    Связывает класс ImageAbout и About'''
    model = ImageAbout
    extra = 1


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "created_at"]
    list_display_links = ("name",)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [ImageAboutInline]


admin.site.register(ContactLink)
admin.site.register(Social)