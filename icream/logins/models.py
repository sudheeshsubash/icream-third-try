from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(User):
    phone_number = models.BigIntegerField(default=None)
    is_block = models.BooleanField(default=None)

    def __str__(self):
        return self.username
        