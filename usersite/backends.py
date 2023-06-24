from django.contrib.auth.models import User ,check_password


class EmailAuthBackend(object):
    def authenticate(self,username=None,password=None):
        try:
            user=User.objects.get(Q)