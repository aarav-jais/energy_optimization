from django.urls import path
from . import views
from .views import renewable_energy_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('home/', views.home_view, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('benchmark/', views.benchmark_view, name='benchmark'),
    path('utility-bills/', views.utility_bill_view, name='utility_bills'),
    path('recommendations/', views.energy_recommendations_view, name='recommendations'),
    path('renewable/', renewable_energy_view, name='renewable-energy'),
    path('energy-analysis/', views.energy_analysis_view, name='energy_analysis'),
]