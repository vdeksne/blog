# Generated by Django 5.0.6 on 2024-06-01 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_alter_blog_blog_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='short_description',
            field=models.TextField(max_length=100),
        ),
    ]