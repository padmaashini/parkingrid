# from django.urls import path, re_path
# from django.conf.urls import include
# from rest_framework.routers import DefaultRouter
# from .views import BuyViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TicketsViewSet

# from . import views
router = DefaultRouter()
router.register(r'tickets', TicketsViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]