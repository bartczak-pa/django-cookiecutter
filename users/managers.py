from typing import Any
from django.contrib.auth.models import BaseUserManager
from django.db.models import QuerySet


class CustomUserManager(BaseUserManager):
    """
    Custom manager for CustomUser model where email is the unique identifier
    for authentication instead of usernames.
    """

    def create_user(self, email: str, password: str | None = None, **extra_fields: Any) -> "CustomUser":
        """
        Create and return a regular user with the given email and password.
        """
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)  # type: ignore [attr-defined]
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str | None = None, **extra_fields: Any) -> "CustomUser":
        """
        Create and return a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

    def get_queryset(self) -> QuerySet:
        """
        Return the default queryset for this manager.
        """
        return super().get_queryset()
