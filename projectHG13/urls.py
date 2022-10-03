from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from appHG13 import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('Psalud/', views.MedicoListView.as_view()),
    path('Psalud/<int:pk>', views.MedicoRetrieveUpdateView.as_view()),
    path('paciente/', views.CrearPacienteView),
    path('familiar/', views.CrearFamiliarView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
]