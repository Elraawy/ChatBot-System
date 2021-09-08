from django.db import models


# Create your models here.
class Conservation(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default="username1")
    content = models.TextField(max_length=500)
    response = models.TextField(max_length=500)

    def __str__(self):
        return self.title
