from django.contrib import admin

from accounts.models import Account, Category, Transaction


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = ["name", "id", "is_active"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = ["name", "id", "account_id"]


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = ["type", "id", "category"]
