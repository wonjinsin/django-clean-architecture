from rest_framework.serializers import ModelSerializer
from model.account.models import Account


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'email', 'name', 'created_at']
