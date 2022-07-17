import uuid
from django.db import models

from django.contrib.auth.models import AbstractUser, UserManager, AnonymousUser as DjangoAnonymousUser


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    objects: UserManager["User"] = UserManager()  # type: ignore[assignment]


class AnonymousUser(DjangoAnonymousUser):
    pass
