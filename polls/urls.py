from django.urls import path, re_path

from . import views
app_name = 'polls'



urlpatterns = [
   
    path('', views.home, name='home'),
    path('endirimurl/<int:id>/', views.endirimurl, name='endirimurl'),
    path('etrafli', views.etrafli, name='etrafli'),
    path('guller', views.guller, name='guller'),
    path('blogumuz', views.blogumuz, name='blogumuz'),
    path('haqqimizda', views.haqqimizda, name='haqqimizda'),
    path('elaqe', views.elaqe, name='elaqe'),
       
]

