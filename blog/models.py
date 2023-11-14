from django.db import models


class Articles(models.Model):
    title = models.SlugField('название')
    content = models.TextField('статья')


    def __str__(self):
        return self.title

# Create your models here.
