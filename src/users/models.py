from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from encrypted_id.models import EncryptedIDModel, EncryptedIDManager


# Create your models here.
# Customized User model.

# class UserManager(BaseUserManager, EncryptedIDManager):
