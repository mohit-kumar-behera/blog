# Generated by Django 3.0.7 on 2020-06-26 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPost', '0004_blog_post_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='blog_title',
            field=models.CharField(default='Title', max_length=100),
        ),
    ]
