# Generated by Django 5.1.4 on 2025-01-01 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_recipe_directions_alter_recipe_ingredients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', max_length=200, unique=True),
        ),
    ]
