from django.contrib.auth.models import User, AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    fio = models.CharField('ФИО', max_length=150)
