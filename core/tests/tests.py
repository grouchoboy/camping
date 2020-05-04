import pytest

from ..models import User


@pytest.mark.django_db
def test_create_user():
    result = User.objects.create_user(email="user@example.com", password="super-secret")
    assert result.email == "user@example.com"
    assert result.check_password("super-secret")
    assert result.password != "super-secret"
