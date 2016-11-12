from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('homesite.urls', namespace='website')),
    url(r'^produtos/', include('products.urls', namespace='products')),
    url(r'^contato/', include('contacts.urls', namespace='contacts')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
