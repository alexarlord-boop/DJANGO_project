from django.db import models


# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    coords = models.TextField()

    type = models.CharField(max_length=50)
    user_skill = models.IntegerField()  # 0-beginner,.., 2-pro
    enviroment_chars = models.IntegerField()  # 0-wild lands,..,2-city
    extreme = models.IntegerField()

    def __str__(self):
        return f'{self.title}  ({self.type})'


class Goal(models.Model):
    activity_id = models.IntegerField()
    activity_title = models.TextField()
    add_data = models.DateField()
    is_done = models.IntegerField()

    def __str__(self):
        return f'{self.activity_title}'
