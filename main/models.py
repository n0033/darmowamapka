from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os


class Style(models.Model):
    name = models.CharField(max_length=20)
    background_image = models.ImageField(null=True, blank=True)
    phone_background_image = models.ImageField(null=True, blank=True)
    font_family = models.CharField(max_length=200, default='palanquin')
    font_color_in_hex = models.CharField(max_length=7, null=True, blank=True)
    currently_used = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Text(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()

    def __str__(self):
        return self.title


class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True)
    checkbox_checked = models.BooleanField(default=False)
    cookie_id = models.CharField(max_length=36)
    ebook_sent = models.BooleanField(default=False)
    video_watched = models.BooleanField(default=False)

    def __str__(self):
        return self.firstname + ' ' + self.lastname + ' | ' + self.email


class Mail(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=78)
    content = models.TextField()
    attachment = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name

