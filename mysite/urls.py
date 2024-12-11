"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from lab import views
from django.views import debug
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


#urlpatterns += staticfiles_urlpatterns()
urlpatterns = [
    path('lab/', include('lab.urls')),
    path('admin/', admin.site.urls),
    path('appointment/', views.appointment),
    path('detail/', views.detail),
    path('', views.index),
    path('blog/', views.blog),
    path('syll/', views.syll),
    path('contact/', views.contact),
    path('facility/', views.facility),
    path('people/', views.people),
    path('test/', views.test),
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

