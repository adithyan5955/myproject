from django.urls import path,include
from django.conf.urls.static import static
from.import views

urlpatterns = [
    path('register/', views.Register, name="register"),
    path('login/', views.Login, name="login"),
    path('logout/', views.logout, name="logout"),

]