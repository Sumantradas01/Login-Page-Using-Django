from django.urls import path
from . import views
urlpatterns = [
    path('test', views.test),
    path('home',views.home),
    path('about',views.about),  
    path('registration',views.registration),
    path('signup',views.signup), 
    path('login',views.login),
    path('log',views.log),
    path('show',views.show),
    path('del/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
    path('editcode/<int:id>',views.edcode),
  
]




