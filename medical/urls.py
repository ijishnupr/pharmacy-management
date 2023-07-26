
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/',include('store.urls')),
    path('storeapi/',include('storeapi.urls')),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
