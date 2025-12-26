from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(TimeStampedModel, AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()


class PriceTag(TimeStampedModel):
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image_storage_location = models.TextField()
