from django.urls import path
from Resortapp import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('member_view/',views.member_view, name='member_view'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('mypage/',views.mypage, name='mypage'),
    path('information/',views.information, name='information'),
    path('edit/', views.edit, name='edit'),
    path('delete/', views.delete, name='delete'),
    path('signuser/', views.signuser, name='signuser'),
    path('hoteldetail/', views.hoteldetail, name='hoteldetail'),
   
    
      
]
