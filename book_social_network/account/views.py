from django.http import HttpResponse
from django.shortcuts import render

from account.forms import LoginForm
from account.utils import authenticate_user


def user_login(request):
    """User authentication page"""

    form = LoginForm(request.POST or None)

    if form.is_valid():
        is_authenticated = authenticate_user(
            request, form.cleaned_data['username'], form.cleaned_data['password'],
        )
        if is_authenticated:
            return HttpResponse('COrrect')
    return render(request, 'account/login.html', {'form': form})
