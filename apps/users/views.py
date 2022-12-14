from rest_framework import generics

from apps.users import serializers
from apps.users.models import UserProfile


class UserProfileList(generics.ListAPIView):
    serializer_class = serializers.InteractionUserSerializer
    queryset = UserProfile.objects.all()

    # authentication_classes = (authentication.ExternTokenAuthentication, ) TODO: uncomment here
    # permission_classes = (IsAuthenticated,) TODO: uncomment here

