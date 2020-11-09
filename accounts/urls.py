from django.urls import path
from accounts import views


urlpatterns = [
    path('', views.index, name='pages/index'),
    path('home/', views.home, name='pages/home'),
    path('profile/', views.profile, name='pages/profile'),
    path('accounts/signup/', views.signup, name='accounts/signup'),
    path('logout/', views.logoutUser, name='logout'),
    path('about/', views.about, name='pages/about'),
    
    
]