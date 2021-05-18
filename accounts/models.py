from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class AccountManager(BaseUserManager):
    def create_user(self, phone, name, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not phone:
            raise ValueError('Users must have a phone')
        
        if not name:
            raise ValueError('Users must have a name')

        user = self.model(
            phone=phone,
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, name, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            phone,
            name,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    phone = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name']

    objects = AccountManager()

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
