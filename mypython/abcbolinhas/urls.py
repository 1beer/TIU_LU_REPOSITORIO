
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('clientes', views.clientes),
     path('produtos', views.produtos),
      path('pedidos', views.pedidos),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
