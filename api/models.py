from django.db import models
from django.core.validators import FileExtensionValidator


def upload_to(instance, filename):
    return filename.format(filename=filename)


class Testimonial(models.Model):
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    name = models.CharField(max_length=150, blank=False)
    company = models.CharField(max_length=100, blank=False)
    title = models.CharField(max_length=200, blank=False)
    text = models.TextField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True, default=0.0)

    def __str__(self):
        return str(self.name)


class Address(models.Model):
    name = models.CharField(max_length=150, blank=False)
    field1 = models.CharField(max_length=100, blank=False)
    field2 = models.CharField(max_length=100, blank=False)
    field3 = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return str(self.name)


class Phone(models.Model):
    name = models.CharField(max_length=100, blank=False)
    number = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return str(self.name)


class Email(models.Model):
    name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(max_length=200, blank=False)

    def __str__(self):
        return str(self.name)


class Team(models.Model):
    name = models.CharField(max_length=200, blank=False)
    title = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Social(models.Model):
    facebook = models.CharField(max_length=200, blank=False)
    twitter = models.CharField(max_length=200, blank=False)
    linkedIn = models.CharField(max_length=200, blank=False)
    instagram = models.CharField(max_length=200, blank=False)
    whatsapp = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return str(self.id)


class Mission(models.Model):
    name = models.CharField(max_length=100, blank=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Vision(models.Model):
    name = models.CharField(max_length=100, blank=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class HomeVideo(models.Model):
    title = models.CharField(max_length=150, blank=True)
    text = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to=upload_to, null=True,
                             validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
