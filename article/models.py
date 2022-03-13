from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.
from markdown import Markdown


class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Tag(models.Model):
    text = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.text

class Avatar(models.Model):
    content = models.ImageField(upload_to='avatar/%Y%m%d')


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='articles'
    )
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='articles'
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='articles'
    )
    avatar = models.ForeignKey(
        Avatar,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='article'
    )



    class Meta:
        ordering = ['-created']

    def get_md(self):
        """markdown"""
        md = Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        md_body = md.convert(self.body)
        return md_body, md.toc

    def __str__(self):
        return self.title
