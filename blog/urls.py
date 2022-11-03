from django.urls import path
from . import views
urlpatterns = [
    path('',views.home ,name = 'blog-home'),
    path('about/', views.about, name='blog-about'),
    path('myprofile/', views.myprofile, name='blog-myprofile'),
    path('newpost/', views.newpost, name = 'blog-newpost'),
    path('mypost/', views.mypost, name= 'blog-mypost'),
    path('fav/<int:id>/', views.favourite_add, name = 'favourite-add'),
    
    path('savedpost/',views.savedpost, name='saved-post')
]