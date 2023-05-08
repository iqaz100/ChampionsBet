from datetime import datetime, timedelta
import jwt
from django.contrib.auth.backends import ModelBackend, UserModel
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.exceptions import MultipleObjectsReturned
from django.db import models
from django.db.models import Q

from main import settings


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, password=None, **extra_fields
    ):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email, password, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    objects = UserManager()
    email = models.EmailField(verbose_name='email address', max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    @property
    def token(self):
        token = jwt.encode({'email': self.email,
                            'exp': datetime.utcnow() + timedelta(days=10)},
                           settings.SECRET_KEY, algorithm='HS256')
        return token


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        except MultipleObjectsReturned:
            return User.objects.filter(email=username).order_by('id').first()
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def get_user(self, user_id):
        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

        return user if self.user_can_authenticate(user) else None
