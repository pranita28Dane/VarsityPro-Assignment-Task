from django.urls import path
from Account.views import register, custom_login, custom_logout, home


urlpatterns = [
    path('home/', home, name='home'),
    path('', register, name='register'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
]

