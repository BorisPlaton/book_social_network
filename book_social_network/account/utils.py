from django.contrib.auth import authenticate, login

from account.models import User


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
    return new_user
