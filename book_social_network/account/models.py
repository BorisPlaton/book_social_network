from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    email = models.EmailField('Email address', unique=True)
    following = models.ManyToManyField(
        'self', through='Subscription', related_name='followers', symmetrical=False, verbose_name="Subscriptions"
    )

    def get_absolute_url(self):
        return reverse('account:user_profile', args=[self.username])

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Profile(models.Model):
    user = models.OneToOneField(verbose_name="User", to=User, on_delete=models.CASCADE, related_name='profile')

    date_of_birth = models.DateField("Birthday", blank=True, null=True)
    photo = models.ImageField("Profile picture", upload_to='users/%Y/%m/%d/', blank=True)

    class Meta:
        verbose_name = 'User profile'
        verbose_name_plural = 'User profiles'

    def __str__(self):
        return f'{self.user.username}'


class Subscription(models.Model):
    user_from = models.ForeignKey(
        User, related_name='subscriptions', on_delete=models.CASCADE, verbose_name='Subscriber'
    )
    user_to = models.ForeignKey(
        User, related_name='subscribers', on_delete=models.CASCADE, verbose_name='Sub'
    )
    subscribe_time = models.DateTimeField("Subscription time", auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-subscribe_time']
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscription'

    def __str__(self):
        return f'{self.user_from.username} follows {self.user_to.username}'
