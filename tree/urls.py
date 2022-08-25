from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from tree.views import *


urlpatterns = [
    # path('makes/', MakeListView.as_view(), name='make_list'),
    # path('', CarListView.as_view(), name='car_list'),
    # path('car/<pk>/', CarDetailView.as_view(), name='car_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)