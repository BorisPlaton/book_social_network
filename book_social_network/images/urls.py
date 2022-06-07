from django.urls import path

from images import views


app_name = 'images'

urlpatterns = [
    path('save_image/', views.save_image, name='save_image'),
    path('image_details/<int:pk>/<slug:slug>/', views.image_detail, name='image_details'),
]
