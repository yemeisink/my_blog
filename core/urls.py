from django.contrib import admin
from django.urls import path,  include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('_blog.urls')),
    path('', include('_podcast.urls'))
]
