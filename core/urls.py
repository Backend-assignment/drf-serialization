from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token # add this
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/auth/', obtain_auth_token), # add this
    
]
