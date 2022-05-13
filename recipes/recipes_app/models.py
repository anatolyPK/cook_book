from django.db import models
from django.urls import reverse


class Recipes(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название блюда")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Рецепт")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True, verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,  null=True, verbose_name="Категория")

    def __srt__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name_plural = 'Рецепты'
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
