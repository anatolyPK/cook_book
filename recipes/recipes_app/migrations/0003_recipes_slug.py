# Generated by Django 4.0.2 on 2022-05-13 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app', '0002_category_recipes_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='slug',
            field=models.SlugField(default=12, max_length=255, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
    ]