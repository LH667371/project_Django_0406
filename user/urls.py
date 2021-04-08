from django.urls import path

from user import views

urlpatterns = [
    path('user/', views.User.as_view()),
    path('user/<str:username>', views.User.as_view()),
    path('register/', views.UserRegister.as_view()),
    path('register/<str:username>', views.UserRegister.as_view()),
]
