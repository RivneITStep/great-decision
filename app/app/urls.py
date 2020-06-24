from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('apartments/', include('apartments.urls')),
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# admin.sites.AdminSite.site_header = 'My site admin header'
# admin.sites.AdminSite.site_title = 'My site admin title'
admin.sites.AdminSite.index_title = 'Great Decision admin'
