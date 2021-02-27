from rest_framework.serializers import HyperlinkedModelSerializer
from .models import ModelUser


class ModelUserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ModelUser
        fields = ['username', 'firstname', 'lastname', 'email']
