from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from account.models import User


class Action(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='actions',
        verbose_name="Author of the action",
        db_index=True,
    )
    description = models.CharField("Action description", max_length=256)
    action_time = models.DateTimeField("Action time", auto_now_add=True)

    target_ct = models.ForeignKey(
        ContentType, blank=True, null=True, related_name='target_obj', on_delete=models.CASCADE
    )
    target_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_ct', 'target_id')

    class Meta:
        ordering = ['-action_time']

    def __str__(self):
        return self.description
