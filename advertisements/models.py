from django.db.models.enums import TextChoices
from django.db.models.base import Model
from django.db.models.fields import TextField, BooleanField
from django.db.models.fields.related import ForeignKey
from django.conf.global_settings import AUTH_USER_MODEL
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField


class AdvertisementStatusChoices(TextChoices):
    """Статусы объявления."""

    OPEN = "OPEN", "Открыто"
    CLOSED = "CLOSED", "Закрыто"
    DRAFT = "DRAFT", "Черновик"


class Advertisement(Model):
    """Объявление."""

    title = TextField()
    description = TextField(default='')
    status = TextField(
        choices=AdvertisementStatusChoices.choices,
        default=AdvertisementStatusChoices.DRAFT
    )
    creator = ForeignKey(
        AUTH_USER_MODEL,
        on_delete=CASCADE,
    )
    created_at = DateTimeField(
        auto_now_add=True
    )
    updated_at = DateTimeField(
        auto_now=True
    )
    favorite = TextField(
        default=''
    )

