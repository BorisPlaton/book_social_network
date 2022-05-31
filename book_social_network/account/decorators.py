from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect


def unauthorized_required(func):
    def check_if_user_if_unauthenticated(request: HttpRequest, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponse('is_authenticated')
        return func(request, *args, **kwargs)

    return check_if_user_if_unauthenticated
