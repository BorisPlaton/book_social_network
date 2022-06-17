from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView, PasswordResetView, \
    PasswordResetConfirmView
from django.urls import path, reverse_lazy

from account import views


app_name = 'account'

urlpatterns = [
    path('edit/', views.edit_profile, name='edit_profile'),
    path('users_list/', views.users_list, name='users_list'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('follow/', views.follow, name='follow'),
    path('registration/', views.registration, name='registration'),
    path('password_change/done/', views.password_change_done, name='change_password_done'),
    path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('reset/done/', views.password_reset_complete, name='password_reset_complete'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path(
        'login/',
        LoginView.as_view(
            redirect_authenticated_user=True,
            template_name='account/registration/login.html',
        ),
        name='login'
    ),
    path(
        'password_change/',
        PasswordChangeView.as_view(
            success_url=reverse_lazy('account:change_password_done'),
            template_name='account/registration/password_change_form.html',
        ),
        name='change_password'
    ),

    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='account/registration/password_reset_form.html',
            email_template_name='account/registration/password_reset_email.html',
            success_url=reverse_lazy('account:password_reset_done'),
        ),
        name='password_reset'
    ),
    path(
        'reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
            template_name='account/registration/password_reset_confirm.html',
            success_url=reverse_lazy('account:password_reset_complete'),
        ),
        name='password_reset_confirm'
    ),
]
