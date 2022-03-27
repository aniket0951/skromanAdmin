"""SkromanAdmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # sales app urls-------this url valid only for sales app functionalities
    path('sales/', include('SalesApp.salesurl')),

    # admin app urls-------this url valid only for admin app functionalities
    path('adminapp/', include('AdminApp.adminurl')),

    # installation app urls-------this url valid only for installation app functionalities
    path('installation/', include('Installation.installationurl')),
]
