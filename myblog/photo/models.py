# -*- coding: utf-8 -*-
from django.db import models
from PIL import Image
from ckeditor.fields import RichTextField

# Crate your models here.

class Article (models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(verbose_name=u'Poster',max_length=256, blank=True, null=True)
    body = RichTextField()
    likes = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = u'Статья'
        verbose_name_plural = u'Статьи'

    def __unicode__(self):
        return unicode(self.title)
    
        
    