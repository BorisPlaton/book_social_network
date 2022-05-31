from django.shortcuts import render

from account.forms import LoginForm


def user_login(request):
    """User authentication page"""

    form = LoginForm(request.POST or None)

    if form.is_valid():
        pass

    return render(request, 'account/login.html', {'form': form})
