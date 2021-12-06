"""PD URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import uzdevumi.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-user', uzdevumi.views.pievienot_lietotaju),
    path('add-user/csv', uzdevumi.views.upload_csv_to_db),
    path('filter-users/user', uzdevumi.views.meklet_lietotaju),
    path('', uzdevumi.views.visi_lietotaji),
    path('user/<int:user_id>', uzdevumi.views.viens_lietotajs, name='viens-lietotajs'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)