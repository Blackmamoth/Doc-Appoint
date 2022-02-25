from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='appointments/login.html', redirect_authenticated_user=True,), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='appointments/login.html'), name='logout'),
    path('appoint/', views.appoint, name='appoint'),
    path('delete/<int:id>', views.delete_appointment, name='delete'),
    path('postpone/<int:id>', views.postpone, name='postpone'),
    path('doctors/', views.doctors, name='doctors'),
]