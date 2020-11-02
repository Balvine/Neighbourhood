from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views



urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^companies/$',views.companies,name = 'companies'),
    url(r'^post/?P<id>(\d)+$',views.post,name='post'),
    url(r'search/',views.search,name='search'),
    url(r'^api/companies/$',views.CompanyList.as_view())

]
