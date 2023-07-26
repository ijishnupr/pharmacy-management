from django.urls import path
from . import views
urlpatterns=[
     path('login', views.login, name='login'),
     path('list',views.medicinedetail,name='list'),
     path('signup',views.signup,name='signup'),
     path('search',views.search),
     path('logout',views.logoutt),
     path('create',views.create),
    path('delete',views.delete),
    path('update',views.update)
]