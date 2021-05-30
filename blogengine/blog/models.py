from django.db import models
from django.urls.base import reverse
from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return f'{new_slug}-{str(int(time()))}'


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')  # у экземпляра кдасса teg при создании этого
    # поля появиться свойство posts, если явно не указать джанго создаст post_set
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})  # reverse (ф-я url в шаблонах) генерирует ссылку,
        # передаем ей назв. юрл шаблона и словарь в качестве ключя - поле по которому мы проводим идентификацию объекта

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
