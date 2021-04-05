from django.urls import path

from employee import views

urlpatterns = [
    path('emplist/', views.EmpAPIView.as_view()),
    path('emplist/<str:id>/', views.EmpAPIView.as_view()),
]
