# Generated by Django 4.2 on 2023-04-07 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_rename_category_post_categories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='postcategory',
            options={'verbose_name': 'Категория новости', 'verbose_name_plural': 'Категории новостей'},
        ),
    ]