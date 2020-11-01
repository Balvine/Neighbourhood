from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    re_path('edit_profile/(?P<username>\w{0,50})',views.edit_profile,name = 'edit_profile'),
    path('companies',views.companies,name = 'companies'),
    re_path('post/(?P<id>\d+)',views.post,name='post'),
    path('search/',views.search,name='search'),
    path('api/companies/',views.CompanyList.as_view())

]
