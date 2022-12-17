from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/post/tag/{self.slug}/'
#카테고리
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name


# 상품 아이템
class Post(models.Model):
    name = models.CharField(max_length=30, unique=True)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    price = models.IntegerField()

    head_image = models.ImageField(upload_to='post/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='post/images/%Y/%m/%d/', blank=True)


    manufacture = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.name}::{self.manufacture}:{self.price}'

    def get_absolute_url(self):
        return f'/post/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} : {self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return 'https://dummyimage.com/50x50/ced4da/6c757d.jpg'

# 제조사
class Manufacture(models.Model):
    name = models.CharField(max_length=30, unique=True)
    address = models.TextField()
    number = models.IntegerField()

    area = models.TextField()


#댓글 모델?
