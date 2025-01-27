from django.urls import path
from .views import views,user_views

urlpatterns = [
    path('',views.home,name="home"),
    path('getdata/',views.getdata,name="getdata"),
    path('sing_up',user_views.sing_up,name="sing_up"),
    path('login',user_views.login,name="login"),
    path('logout',user_views.logout_user,name="logout"),
]
