from django.db import models


# Create your models here.
class Places(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    type = models.CharField(max_length=50)
    user_skill = models.IntegerField()  # 0-beginner,.., 2-pro
    enviroment_chars = models.IntegerField()  # 0-wild lands,..,2-city
    extreme = models.IntegerField()

    def __str__(self):
        return self.type
