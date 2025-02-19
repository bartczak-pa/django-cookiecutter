from typing import Any
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)  # Use email as the unique identifier

    USERNAME_FIELD = 'email'  # Set email as the primary field for authentication
    REQUIRED_FIELDS: list[str] = []  # No additional fields are required

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email
