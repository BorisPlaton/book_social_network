from django.urls import path

from actions import views


app_name = 'actions'

urlpatterns = [
    path('action_pagination/', views.get_action_pagination, name='action_pagination')
]
