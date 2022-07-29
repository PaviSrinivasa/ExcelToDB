from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path('genelist/home', views.home, name='home'),
    path('genelist/addGene', views.addGene, name='addGene'),
    path('genelist/addLiterature', views.addLiterature, name='addLiterature'),
    path('/show/$', views.showAuthor, name='showAuthor'),
    #path('webexptrack/search', views.search, name='search'),
    #path('webexptrack/show/<int:id>/', views.show_exp, name='show_exp'),
    #path('webexptrackaccounts/', include('django.contrib.auth.urls')),
    #path('login/', include('django.contrib.auth.urls')),    #path('logout/', include('django.contrib.auth.urls')),
  #  path('accounts/logout', include('django.contrib.auth.urls')),
]
