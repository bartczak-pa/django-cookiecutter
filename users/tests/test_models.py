from django.contrib.auth import get_user_model
import pytest

User = get_user_model()


@pytest.mark.django_db
class TestCustomUserModel:
    def test_user_creation(self) -> None:
        """Test that a regular user is created with the correct attributes."""
        user = User.objects.create_user(
            email="testuser@example.com",
            password="testpassword",
            first_name="Test",
            last_name="User",
        )
        assert user.email == "testuser@example.com"
        assert user.check_password("testpassword")
        assert not user.is_staff
        assert not user.is_superuser

    def test_create_user_without_email_raises_error(self) -> None:
        """Test that creating a user without an email raises a ValueError."""
        with pytest.raises(ValueError, match="The Email field must be set"):
            User.objects.create_user(email="", password="testpassword")

    def test_create_superuser(self) -> None:
        """Test that a superuser is created with the correct attributes."""
        admin_user = User.objects.create_superuser(
            email="admin@example.com",
            password="adminpassword",
        )
        assert admin_user.email == "admin@example.com"
        assert admin_user.is_staff
        assert admin_user.is_superuser

    def test_string_representation(self) -> None:
        """Test the string representation of the custom user model."""
        user = User.objects.create_user(
            email="testuser@example.com", password="testpassword"
        )
        assert str(user) == "testuser@example.com"

    def test_email_normalization(self) -> None:
        """Test that email addresses are normalized (lowercase)."""
        user = User.objects.create_user(
            email="TESTUSER@EXAMPLE.COM", password="testpassword"
        )
        assert user.email == "testuser@example.com"

    def test_duplicate_email_raises_error(self) -> None:
        """Test that creating a user with a duplicate email raises an IntegrityError."""
        User.objects.create_user(email="testuser@example.com", password="testpassword")
        with pytest.raises(Exception):  # Replace Exception with IntegrityError if using PostgreSQL
            User.objects.create_user(email="testuser@example.com", password="anotherpassword")
