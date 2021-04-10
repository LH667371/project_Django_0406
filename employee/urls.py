from django.urls import path

from employee import views

urlpatterns = [
    path('emplist/', views.EmpAPIView.as_view()),
    path('emplist/<str:pk>/', views.EmpAPIView.as_view()),
    path('department/', views.DepartAPIView.as_view()),
    path('department/<str:pk>/', views.DepartAPIView.as_view()),
    path('search/', views.SerchEmpAPIView.as_view()),
]
