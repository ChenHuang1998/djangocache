from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    class Meta:
        db_table = "user_info"