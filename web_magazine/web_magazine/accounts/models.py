from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import re

from web_magazine.book.models import validate_max_size

def validate_max_size_profile_picture(cover):
    MAX_UPLOAD_SIZE = 1 * 1024 * 1024

    if cover.size > MAX_UPLOAD_SIZE:
        raise ValidationError("The book size must not exceed 5MB")

def phone_regex_validator(value):
    if not re.match(r'^\+\d{1,15}$', value):
        raise ValidationError("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class AppUser(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )


    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users'

    objects = UserManager()


class Profile(models.Model):
    GENDER_CHOICES = (
        ("Male",'Male'),
        ("Female",'Female'),
        ("Do not show", 'Do not show')
    )



    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    profile_picture = models.ImageField(
        upload_to='profile-picture',
        blank=True,
        null=True,
        validators=[validate_max_size_profile_picture,],
    )

    gender = models.CharField(
        blank=True,
        null=True,
        max_length=11,
        choices=GENDER_CHOICES,
    )

    phone =models.CharField(
        validators=[phone_regex_validator,],
        max_length=17,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    user = models.OneToOneField(AppUser,on_delete=models.CASCADE,
                                primary_key=True,)










@receiver(post_save, sender=AppUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()