# Generated by Django 3.0.7 on 2020-06-28 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPost', '0006_auto_20200627_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='blog_image',
            field=models.ImageField(blank=True, upload_to='image/'),
        ),
    ]
