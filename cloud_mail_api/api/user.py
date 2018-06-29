__all__ = ["UserMethodsGroup"]

import os.path

from .. import constants
from .. import errors

class UserMethodsGroup:
    __slots__ = ["cloud_mail_instance", "api"]
    def __init__(self, cloud_mail_instance, api_instance):
        self.cloud_mail_instance = cloud_mail_instance
        self.api = api_instance

    def __call__(self):
        url = constants.API_USER_PATH

        data = {
            "token": self.api.csrf_token
        }

        return self.api(url, "get", params=data)

    def space(self):
        url = constants.API_USER_SPACE_PATH

        data = {
            "token": self.api.csrf_token
        }

        return self.api(url, "get", params=data)