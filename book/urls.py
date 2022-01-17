from book import views
from django.urls import path
urlpatterns = [
    path('',views.home,name="homepage"),
    path('login/',views.loginView,name="login"),
    path('sign_up/',views.sign_up,name="sign_up"),
    path('logout/',views.logout,name="logout"),
]
