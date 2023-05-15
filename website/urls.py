from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from articles.views import articles_list

urlpatterns = [
    path('', articles_list),
    path('admin/', admin.site.urls),
]
