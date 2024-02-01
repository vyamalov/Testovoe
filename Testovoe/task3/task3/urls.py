from django.contrib import admin
from django.urls import path
from azs.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('azs/', AZSAPIView.as_view())
]
