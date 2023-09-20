from rest_framework.serializers import ModelSerializer

from subscr.models import UserProfule


class UserProfileSerializers(ModelSerializer):
    class Meta:
        model = UserProfule
        fields = '__all__'