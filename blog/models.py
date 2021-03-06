# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render




class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    exp = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to = 'blog/static/subidas/img', default = 'blog/static/css/imagenes/pelota.png')
    nombre_imagen = models.CharField(max_length=80)
    CATEGORIAS = (
        ("0", 'Trabajos Practicos'),
        ("1", 'Ejemplo'),        
        ("2", 'Otros'),
    )
    categorias = models.CharField(max_length=6,
                                      choices=CATEGORIAS,
                                      default="0")
    url_post = models.CharField(max_length=60, null=True, blank=True)
    
    def __unicode__(self):
        return self.title



### Admin

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    display_fields = ["title", "created","categorias","exp","nombre_imagen","imagen",]
     
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))
