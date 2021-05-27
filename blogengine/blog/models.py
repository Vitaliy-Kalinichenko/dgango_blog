from django.db import models
from django.urls.base import reverse


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('posts_detail', kwargs={'slug': self.slug})  # reverse (ф-я url в шаблонах) генерирует ссылку,
        # передаем ей назв. юрл шаблона и словарь в качестве ключя - поле по которому мы проводим идентификацию объекта

    def __str__(self):
        return self.title
