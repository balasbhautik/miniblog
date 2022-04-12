from django.urls import path
from . import views
urlpatterns = [
     path('', views.home, name='Home'),
     path('about/', views.about, name='AboutUs'),
     path('contact/', views.contact, name='ContactUs'),
     path('dashboard/', views.dashboard,name='Dashboard'),
     path('login/', views.user_login, name='Login'),
     path('signup/', views.user_signup, name='Signup'),
     path('logout/', views.user_logout, name='Logout'),
     path('addpost/', views.add_post, name='AddPost'),
     path('updatepost/<int:id>/', views.update_post, name='UpdatePost'),
     path('delete/<int:id>/', views.delete_post, name='DeletePost')

]
