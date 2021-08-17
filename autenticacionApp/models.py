from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, phone_number, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.email  = email
        user.first_name = first_name
        user.last_name = last_name
        user.phone_number = phone_number
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, phone_number, password, email):
        user = self.create_user(username = username, email = email, first_name = first_name, last_name = last_name, phone_number = phone_number, password = password)
        user.is_superuser = True
        user.save(using=self._db)
        return user

class restauranteUser(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Nombre de usuario', max_length = 15, unique=True)
    password = models.CharField('Contraseña', max_length = 256)
    email = models.EmailField('Correo electrónico', max_length = 50)
    first_name = models.CharField('Nombres', max_length = 50)
    last_name = models.CharField('Apellidos', max_length = 50)
    phone_number = models.BigIntegerField('Número de teléfono')
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'phone_number']