# Generated by Django 5.1.2 on 2024-11-01 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmIdeas', '0002_idea_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='slug',
            field=models.SlugField(default='agri-idea'),
        ),
    ]