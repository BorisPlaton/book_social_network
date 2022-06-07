from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField("Email address", unique=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    # def is_authenticated_via_oauth(self):
    #     return self in



class Profile(models.Model):
    user = models.OneToOneField(verbose_name="User", to=User, on_delete=models.CASCADE, related_name='profile')

    date_of_birth = models.DateField("Birthday", blank=True, null=True)
    photo = models.ImageField("Profile picture", upload_to='users/%Y/%m/%d/', blank=True)

    class Meta:
        verbose_name = 'User profile'
        verbose_name_plural = 'User profiles'

    def __str__(self):
        return f'{self.user.username}'
