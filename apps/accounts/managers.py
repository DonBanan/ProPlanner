from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, first_name=None, last_name=None, middle_name=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, middle_name=middle_name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, first_name=None, last_name=None, middle_name=None):
        user = self.create_user(email=email, first_name=first_name, last_name=last_name, middle_name=middle_name,
                                password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
