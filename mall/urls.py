from django.urls import path, include
from rest_framework import routers

from mall import views

router = routers.DefaultRouter()
router.register(r'company', views.COMPANYViewSet)

urlpatterns = [
    path('',include(router.urls)),
]