from django.conf.urls import *
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
# from django.urls import path, include
# from rest_framework import routers

# from mall import views
#
# router = routers.DefaultRouter()
# router.register(r'company', views.COMPANYViewSet)
#
# urlpatterns = [
#     path('',include(router.urls)),
# ]

urlpatterns = []

activityUrlPattern = [
    url(r'^find/$', activity.ActivityFind.as_view(), name="activity.ActivityFind"),
]

qaUrlPattern = [
    url(r'^find/$', qa.QaFind.as_view(), name="qa.QaFind"),
]

productUrlPattern = [
    url(r'^find/$', product.ProductFind.as_view(), name="product.ProductFind"),
]

areaUrlPattern = [
    url(r'^find/$', address.AreaFind.as_view(), name="address.AreaFind"),
]

addressUrlPattern = [
    url(r'^find/$', address.AddressFind.as_view(), name="address.AddressFind"),
    url(r'^new/$', address.AddressNew.as_view(), name="address.AddressNew"),
    url(r'^(\w+)/$', address.Address.as_view(), name="address.Address"),
]

restUrlPatterns = [
    url(r'^activity/', include(activityUrlPattern)),
    url(r'^qa/', include(qaUrlPattern)),
    url(r'^product/', include(productUrlPattern)),
    url(r'^area/', include(areaUrlPattern)),
    url(r'^address/', include(addressUrlPattern)),
]

restUrlPatterns = format_suffix_patterns(restUrlPatterns)
urlpatterns += restUrlPatterns