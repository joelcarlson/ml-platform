from django.conf.urls import url
from manuscript_matcher import views

urlpatterns = [
    url(r'^journals/$', views.journal_list),
    url(r'^journals/(?P<pk>[0-9]+)/$', views.journal_detail),
]