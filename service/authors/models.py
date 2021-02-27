from django.db import models
from uuid import uuid4

class ModelUser(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    username = models.CharField(max_length=32)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.EmailField(max_length=254, unique=True)


    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'



