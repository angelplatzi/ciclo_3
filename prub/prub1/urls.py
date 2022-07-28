
from django.contrib import admin
from django.urls import path, include
from tienda import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", include('loginandregistrer.urls')),
    path('tienda/',include('tienda.urls'))
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)