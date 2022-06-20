from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from images.models import Image


@receiver(m2m_changed, sender=Image.user_likes.through)
def update_likes_amount(sender, instance, **kwargs):
    instance.total_likes = instance.user_likes.count()
    instance.save()
