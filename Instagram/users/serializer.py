from rest_framework.serializers import ModelSerializer
from users.models import Account


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ['__all__']
