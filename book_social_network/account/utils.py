from django.contrib.auth import authenticate, login


def authenticate_user(request, username: str, password: str) -> bool | None:
    """Авторизовывает пользователя по логину и паролю"""

    user = authenticate(username=username, password=password)
    if user and user.is_active:
        login(request, user)
        return True


