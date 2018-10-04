"""eLearningSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path
from django.utils.translation import gettext_lazy as _

# urlpatterns = [
#     path('eLearning/', include('eLearning.urls')),
#     path('admin/', admin.site.urls)
# ]

admin.site.index_title = _('Administración del Sitio')
admin.site.site_header = _('eLearning - Panel Administrativo')
admin.site.site_title = _('Administración del Sitio')

urlpatterns = i18n_patterns(
    path('eLearning/', include('eLearning.urls')),
    path('admin/', admin.site.urls),
    # If no prefix is given, use the default language
    prefix_default_language=False,
)
