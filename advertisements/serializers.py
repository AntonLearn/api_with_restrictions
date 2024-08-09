from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from advertisements.models import Advertisement
from rest_framework.validators import ValidationError

class UserSerializer(ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = '__all__'

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user

        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        user = self.context['request'].user
        # Проверяем что пользователь имеет менее 10 объявлений
        # self.instance отсутствует если объект создается.
        # Это условие нужно чтобы проходила валидация при редактировании
        if not self.instance:
            if len(Advertisement.objects.filter(creator=user) & Advertisement.objects.filter(status='OPEN')) >= 10:
                raise ValidationError(f'User {user} can\'t create more then 10 items!')

        return data



