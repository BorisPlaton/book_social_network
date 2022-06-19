from datetime import timedelta

from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

from account.models import User
from actions.models import Action


def get_followed_users_actions(user: User):
    return (Action.objects
            .filter(user__pk__in=user.following.values_list('id', flat=True))
            .exclude(user=user)
            .select_related('user__profile')
            .prefetch_related('target'))


def create_action(user, description, target=None) -> bool:
    last_minute = timezone.now() - timedelta(seconds=60)
    similar_actions = Action.objects.filter(
        user=user,
        description=description,
        action_time__gte=last_minute
    )
    if target:
        similar_actions = similar_actions.filter(
            target_ct=ContentType.objects.get_for_model(target),
            target_id=target.pk,
        )
    if similar_actions.exists():
        return False

    Action.objects.create(user=user, description=description, target=target)

    return True
