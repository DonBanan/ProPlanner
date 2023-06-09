from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return '{0} {1} {2}'.format(self.last_name, self.first_name, self.middle_name)

    def get_short_name(self):
        if self.middle_name:
            return '{0} {1}. {2}.'.format(self.last_name, self.first_name[0], self.middle_name[0])
        else:
            return '{0} {1}.'.format(self.last_name, self.first_name[0])

    def __str__(self):
        return self.email
