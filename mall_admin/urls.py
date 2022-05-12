"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from .views import *
from mall.views import activity as act
from mall.views import product as pro
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = []

activityUrlPattern = [
    url(r'^find/$', act.ActivityFind.as_view(), name="act.ActivityFind"),
    url(r'^new/$', activity.ActivityNew.as_view(), name="activity.ActivityNew"),
    url(r'^(\w+)/$', activity.Activity.as_view(), name="activity.Activity"),
]

qaUrlPattern = [
    url(r'^find/$', qa.QaFind.as_view(), name="qa.QaFind"),
    url(r'^new/$', qa.QaNew.as_view(), name="qa.QaNew"),
    url(r'^(\w+)/$', qa.Qa.as_view(), name="qa.Qa"),
]

productUrlPattern = [
    url(r'^find/$', pro.ProductFind.as_view(), name="product.ProductFind"),
    url(r'^new/$', product.ProductNew.as_view(), name="product.ProductNew"),
    url(r'^public/$', product.ProductPublic.as_view(), name="product.ProductPublic"),
    url(r'^(\w+)/$', product.Product.as_view(), name="product.Qa"),
]

discountUrlPattern = [
    url(r'^find/$', discount.DiscountFind.as_view(), name="discount.DiscountFind"),
    url(r'^new/$', discount.DiscountNew.as_view(), name="discount.DiscountNew"),
    url(r'^(\w+)/$', discount.Discount.as_view(), name="discount.Discount"),
]

couponUrlPattern = [
    url(r'^find/$', coupon.CouponFind.as_view(), name="coupon.CouponFind"),
    url(r'^new/$', coupon.CouponNew.as_view(), name="coupon.CouponNew"),
    url(r'^(\w+)/$', coupon.Coupon.as_view(), name="coupon.Coupon"),
]

restUrlPatterns = [
    url(r'^activity/', include(activityUrlPattern)),
    url(r'^qa/', include(qaUrlPattern)),
    url(r'^discount/', include(discountUrlPattern)),
    url(r'^coupon/', include(couponUrlPattern)),
    url(r'^product/', include(productUrlPattern)),
]

restUrlPatterns = format_suffix_patterns(restUrlPatterns)
urlpatterns += restUrlPatterns
