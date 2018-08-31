# -*- coding: utf-8 -*-
# from django.contrib.auth.models import User
from django.db.models import Q
from views import User


class EmailAuthBackend(object):
    def authenticate(self, username, password):
        try:
            print username, password, "111111111111111111111111111"
            user = User.objects.get(Q(username=username) | Q(email=username))

            if user.check_password(password):
                return user
        except Exception as e:
            return None
