# Generated by Django 3.0.7 on 2020-06-26 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPost', '0003_blog_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='blog_title',
            field=models.CharField(default='Title', max_length=50),
        ),
    ]
