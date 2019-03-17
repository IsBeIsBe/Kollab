"""kollab_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from kollab import views, urls
from django.conf import settings
from django.conf.urls.static import static

LOGIN_URL = 'login'

LOGOUT_URL = 'logout'

LOGIN_REDIRECT_URL = 'home'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_page, name='login_page'),
    url(r'^firststep/', views.login_register, name='login_register'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    
    # the below ensures that all urls that start 
    # with kollab are dealt with by the urls.py in 
    # the kollab folder
    url(r'^kollab/', include(urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

