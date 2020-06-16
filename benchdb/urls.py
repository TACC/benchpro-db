"""benchdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from results.views import result_detail_view, result_create_view, result_delete_view, result_list_view

urlpatterns = [
    path('', result_list_view, name='home'),
    path('result/<int:id>/', result_detail_view),
    path('result/<int:id>/delete', result_delete_view),
    path('create/', result_create_view),
    path('admin/', admin.site.urls),
]
