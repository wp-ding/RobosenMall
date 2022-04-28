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

restUrlPatterns = [
    url(r'^activity/', include(activityUrlPattern)),
    url(r'^qa/', include(qaUrlPattern)),
]

restUrlPatterns = format_suffix_patterns(restUrlPatterns)
urlpatterns += restUrlPatterns