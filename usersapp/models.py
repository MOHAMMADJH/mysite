from unicodedata import name
from django.db import models
import uuid

# Create your models here.

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

class UserManager(BaseUserManager):


    def create_user(self, email, password=None, **extra_fields):
      """Create, save and return a new user."""
      if not email:
          raise ValueError('User must have an email address.')
      user = self.model(email=self.normalize_email(email), **extra_fields)
      user.set_password(password)
      user.save(using=self._db)

      return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()




class note(models.Model):
    """
      class Note models field
    """

    note_id = models.UUIDField(default=uuid.uuid4, editable=False)
    note = models.TextField()
    # key = models.CharField(max_length=250, blank=True)
    email = models.EmailField(null=True, max_length=200, blank=True)
    password = models.CharField(null=True, max_length=200, blank=True )
    date_c = models.DateTimeField(null=True, auto_now_add=True)
    self_d = models.DateTimeField(null=True, blank=True)
    note_name = models.CharField(null=True, max_length=100, blank=True)
    is_d = models.BooleanField(null=True, default=False)

    def __str__(self):
        return str(self.email)


  




class myuser(models.Model):
    name = models.CharField(max_length=90)
    
