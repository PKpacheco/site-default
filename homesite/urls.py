from django.conf.urls import url
from .views import HomeSiteView

urlpatterns = [
    url(r'^$', HomeSiteView.as_view(), name='home'), ]
