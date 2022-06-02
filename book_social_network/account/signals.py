from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models import Profile


@receiver(post_save, sender=get_user_model(), dispatch_uid='create_user_profile')
def create_user_profile(sender, **kwargs):
    if kwargs.get('created'):
        Profile.objects.create(user=kwargs.get('instance'))
