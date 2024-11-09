from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, nombre, apellido, password=None, **extra_fields):
        if not username:
            raise ValueError('The Email field must be set')
        
        username = self.normalize_email(username)
        user = self.model(username=username, nombre=nombre, apellido=apellido, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, nombre, apellido, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, nombre, apellido, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.EmailField(('email address'), unique=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD ='username'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    def __str__(self):
        return self.username