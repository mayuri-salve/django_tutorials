from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from companies import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^stocks/', views.stocklist.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
