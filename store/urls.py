from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('signup',views.signup,name='signupp'),
    path('Logoutpage',views.Logoutpage,name='logoutpage'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('listview',views.medlist.as_view(),name='listview'),
    path('create',views.midcreate,name='create'),
    path('update/<int:pk>',views.midupdate.as_view(),name='update'),
    path('delete/<int:pk>',views.middelete.as_view(),name='delete'),
    path('search',views.search,name='search'),
    path('about',views.about,name='about'),
    path('detail/<int:pk>',views.meddetail,name='detailview'),
    
]