from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from account.decorators import unauthorized_required
from account.forms import LoginForm
from account.utils import authenticate_user


@unauthorized_required
def user_login(request):
    """User authentication page"""

    form = LoginForm(request.POST or None)

    if form.is_valid():
        is_active = authenticate_user(
            request, form.cleaned_data['username'], form.cleaned_data['password'],
        )
        if is_active:
            return HttpResponse('correct')
    return render(request, 'account/login.html', {'form': form})


@login_required
def user_logout(request):
    """Выход из аккаунта пользователя"""

    logout(request)
    return redirect('account:user_login')
