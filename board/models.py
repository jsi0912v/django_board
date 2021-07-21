from django.db import models

# Create your models here.
class Post(models.Model):
    postname = models.CharField(max_length=50)
    content = models.TextField()
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.postname