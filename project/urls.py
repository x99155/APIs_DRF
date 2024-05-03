from django.contrib import admin
from django.urls import path, include

from shop.views import CategoryAPIView, ProductAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/category/', CategoryAPIView.as_view()), # crée l'url et on l'associe à notre vue
    path('api/product/', ProductAPIView.as_view())
]
