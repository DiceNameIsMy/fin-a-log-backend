import uuid

from django.db import models

from users.models import User


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="accounts")
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=20, decimal_places=2)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "accounts"

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name="categories")
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "categories"

    def __str__(self) -> str:
        return self.name


class TransactionType(models.TextChoices):
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"
    TRANSFER = "TRANSFER"


class Transaction(models.Model):
    Type = TransactionType

    sender = models.ForeignKey(Account, on_delete=models.PROTECT, null=True, related_name="sent_transactions")
    receiver = models.ForeignKey(Account, on_delete=models.PROTECT, null=True, related_name="received_transactions")
    type = models.CharField(max_length=20, choices=Type.choices)

    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="transactions")
    amount = models.DecimalField(max_digits=17, decimal_places=2)

    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "transactions"

    def __str__(self) -> str:
        return f"{self.type}: {self.amount}"
