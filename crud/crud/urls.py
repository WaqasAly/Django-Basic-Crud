"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import create_product
from .views import delete_product
from .views import product_list
from .views import update_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', create_product, name='create_product'),
    path('', product_list, name='product_list'),
    path('delete/<int:product_id>/', delete_product, name='delete_product'),
    path('update/<int:product_id>/', update_product, name='update_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

