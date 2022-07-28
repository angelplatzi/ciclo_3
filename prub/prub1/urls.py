
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from prub1.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path("register/", include('registrer.urls')),
    path('tienda/',include('tienda.urls')),
    path('carro/',include('carro.urls'))
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
