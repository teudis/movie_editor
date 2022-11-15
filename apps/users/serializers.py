from rest_framework import serializers

from apps.users.models import InteractionUser


class InteractionUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = InteractionUser
        fields = ('id', 'email', 'screen_name', )
