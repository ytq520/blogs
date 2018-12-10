from django.db import models


class MyUser(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'


class ArticleType(models.Model):
    t_name = models.CharField(max_length=20, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'article_type'


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)
    content = models.TextField(null=True)
    upload_time = models.DateTimeField(auto_now_add=True)
    tf = models.ForeignKey(ArticleType)

    class Meta:
        db_table = 'article'



