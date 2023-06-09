# Generated by Django 4.2 on 2023-04-12 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0004_alter_author_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.AlterModelOptions(
            name='postcategory',
            options={},
        ),
        migrations.RenameField(
            model_name='author',
            old_name='user',
            new_name='authorUser',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='commentPost',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='commentUser',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created',
            new_name='dateCreation',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created',
            new_name='dateCreation',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='categories',
            new_name='postCategory',
        ),
        migrations.RenameField(
            model_name='postcategory',
            old_name='category',
            new_name='categoryThrough',
        ),
        migrations.RenameField(
            model_name='postcategory',
            old_name='post',
            new_name='postThrough',
        ),
        migrations.RemoveField(
            model_name='author',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='post',
            name='isnews',
        ),
        migrations.AddField(
            model_name='author',
            name='ratingAuthor',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='categoryType',
            field=models.CharField(choices=[('NW', 'Новость'), ('AR', 'Статья')], default='AR', max_length=2),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=128),
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='news.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(related_name='categories', through='news.Subscriber', to=settings.AUTH_USER_MODEL),
        ),
    ]
