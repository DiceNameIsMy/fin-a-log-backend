from typing import Callable
import pytest

from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework.response import Response

from users.models import User


PROFILE_URL = reverse("profile")


@pytest.mark.django_db
def test_valid(api: APIClient, authorize: Callable[[APIClient, User], None], user: User) -> None:
    authorize(api, user)
    r: Response = api.get(PROFILE_URL)

    assert r.status_code == 200, r.data
    assert set(r.data.keys()) == {
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
        "is_active",
        "date_joined",
    }


@pytest.mark.django_db
def test_not_authenticated(api: APIClient, user: User) -> None:
    r: Response = api.get(PROFILE_URL)

    assert r.status_code == 401, r.data
    assert r.data == {"detail": "Authentication credentials were not provided."}
