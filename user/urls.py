from django.urls import path

from user import views

urlpatterns = [
    path('user/', views.User.as_view()),
    path('user/<str:username>', views.User.as_view()),
    path('captcha/', views.Captcha.as_view()),
]
