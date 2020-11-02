from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.index, name='landing'),
    # url(r'^signup/$', views.signup, name='signup'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate, name='activate'),
    url(r'^createhood/$', views.createhood, name='createhood'),
    url(r'^edithood/(\d+)$', views.edithood, name='edithood'),
    url(r'^deletehood/(\d+)$',views.delhood, name = 'deletehood'),
    url(r'^join/(\d+)$',views.join, name = 'joinhood'),
    url(r'^createbusiness/$', views.createbiz, name='createbiz'),
    url(r'^exithood/(\d+)$', views.exithood, name='exithood'),
    url(r'^createpost/$', views.createPost, name='createpost'),
    url(r'^user/(\d+)$', views.profile, name='profile'),
    url(r'search/', views.search_results, name='search_results'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)