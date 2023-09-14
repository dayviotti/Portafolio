from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('educacion', views.educacion),
    path('experiencia', views.experiencia),
    path('proyecto', views.proyecto),
    path('login/', views.login_view, name='login'),
    path('send_email/', views.send_email, name='send_email'),
]
