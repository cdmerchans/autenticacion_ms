"""autenticacionProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from autenticacionApp.views import VerifyTokenView
from autenticacionApp.views import CrearUsuario, ConsultarUsuario, BuscarUsuario
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url 

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(),name='login'),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', VerifyTokenView.as_view()),
    path('registro/', csrf_exempt(CrearUsuario.as_view())),
    path('actualizar', csrf_exempt(ConsultarUsuario.as_view())),
    url(r'buscar/(?P<pk>[0-9]+)$', csrf_exempt(BuscarUsuario.as_view())),
]

