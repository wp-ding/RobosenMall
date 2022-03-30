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
    url(r'^new/$', activity.ActivityNew.as_view(), name="activity.ActivityNew"),
    url(r'^(\w+)/$', activity.Activity.as_view(), name="activity.Activity"),
]

restUrlPatterns = [
    url(r'^activity/', include(activityUrlPattern)),
]

restUrlPatterns = format_suffix_patterns(restUrlPatterns)
urlpatterns += restUrlPatterns