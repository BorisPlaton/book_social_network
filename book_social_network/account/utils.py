from django.contrib.auth import authenticate, login

from account.models import User, Subscription
from actions.models import Action
from actions.utils import create_action


def authenticate_user(request, username: str, password: str) -> bool | None:
    """Авторизует пользователя по логину и паролю"""

    user = authenticate(username=username, password=password)
    if user and user.is_active:
        login(request, user)
        return True


def create_user_and_profile(username: str, email: str, password: str) -> User:
    new_user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
    )
    create_action(new_user, "register account")
    return new_user


def subscribe_user(user_follower: User, followed_user: User, subscribe: bool):
    if subscribe:
        Subscription.objects.get_or_create(user_from=user_follower, user_to=followed_user)
        create_action(user_follower, "started following", followed_user)
    else:
        Subscription.objects.filter(user_from=user_follower, user_to=followed_user).delete()
