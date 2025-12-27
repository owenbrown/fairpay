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
    store_visit = models.ForeignKey("StoreVisit", on_delete=models.CASCADE)


class Receipt(TimeStampedModel):
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image_storage_location = models.TextField()
    store_visit = models.ForeignKey("StoreVisit", on_delete=models.CASCADE)


class StoreVisit(TimeStampedModel):
    """Conceptually, a trip to a retailer. All PriceTag associated with a visit should match the Receipt associated with a store visit, or the user is being overcharged."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
