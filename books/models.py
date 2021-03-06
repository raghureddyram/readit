from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, help_text="Use pen name, not real name")
    review = models.TextField(blank=True, null=True)
    date_reviewed = models.DateTimeField(blank=True, null=True)
    is_favorite = models.BooleanField(default=False, verbose_name="Favorite?")


    def __str__(self):
        return self.title
