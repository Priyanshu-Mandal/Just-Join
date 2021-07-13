from django.urls import path
from . import views


urlpatterns=[
    path('', views.home, name='home'),
    path('register',views.register,name="register"),
    path('enter',views.enter,name="enter"),
    path('offerride',views.offerride,name="offerride"),
    path('getride',views.getride,name="getride"),
    path('logout',views.logout,name="logout")
]
