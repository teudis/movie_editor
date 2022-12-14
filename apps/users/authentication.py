from django.contrib.auth import get_user_model

import requests
from drf_spectacular.extensions import OpenApiAuthenticationExtension
from drf_spectacular.plumbing import build_bearer_security_scheme_object
from rest_framework import authentication
from rest_framework import exceptions

# endpoint to get the users type SYSTEM from external api
from apps.users.models import UserProfile

SYSTEM_USER_DATA_ENDPOINT = "https://dev-wbe.watchity.net/rest-auth/user/"


class ExternTokenAuthentication(authentication.TokenAuthentication):
    """"
    Custom Authentication method that use an url (SYSTEM_USER_DATA_ENDPOINT) to obtain users data sending a token
    provided in header of request.
    """

    @staticmethod
    def user_data_is_valid(json_response: dict) -> bool:
        """" Check if json_response is valid and contain needed data for authenticated users """
        expected_keys = [
            'username',
            'email',
            'screen_name',
        ]
        if not type(json_response) == dict:
            return False
        for expected_key in expected_keys:
            if expected_key not in json_response.keys():
                return False
        return True

    def authenticate(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION', None)
        if not auth:
            return None
        try:
            auth_method, value = auth.split()
            if auth_method == 'Token':
                try:
                    headers = {
                        'Authorization': auth,
                        'Accept': 'application/json',
                    }
                    response = requests.get(SYSTEM_USER_DATA_ENDPOINT, headers=headers)
                    if response.status_code == 200:
                        user_data = response.json()
                        if not self.user_data_is_valid(user_data):
                            exceptions.AuthenticationFailed("Wrong response from remote server ", user_data)
                        else:
                            user, create = get_user_model().objects.get_or_create(username=user_data.get('username'))
                            user.email = user_data.get('email')
                            user.save()
                            try:
                                user_profile = UserProfile.objects.get(user=user)
                                user_profile.screen_name = user_data.get('screen_name')
                                user_profile.save()
                            except UserProfile.DoesNotExist:
                                UserProfile.objects.create(user=user,
                                                           screen_name=user_data.get('screen_name'),
                                                           )
                            return user, None
                    else:
                        raise exceptions.AuthenticationFailed()
                except requests.exceptions.ConnectionError:
                    raise exceptions.AuthenticationFailed('Connection error')
            return None
        except ValueError:
            return None