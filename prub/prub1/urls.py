
from django.contrib import admin
from django.urls import path, include
from tienda import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.contrib.auth.urls import urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", include('loginandregistrer.urls')),
    path('tienda/',include('tienda.urls')),
    path('', include('login.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
