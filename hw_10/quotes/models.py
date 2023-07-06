from django.db import models
from django.urls import reverse
# from django.utils import timezone

# Create your models here.

# created_default = timezone.now()


class Author(models.Model):
    fullname = models.CharField(max_length=128, unique=True, null=True, blank=True)
    born_date = models.CharField(max_length=40)
    born_location = models.CharField(max_length=128)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse('quotes:about', kwargs={'author_id': self.pk})


class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    tags = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('quotes:quote', kwargs={'quote_id': self.pk})

    def __str__(self):
        return self.quote
