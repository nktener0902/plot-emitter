from django.urls import path
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views


app_name = 'accounts'
urlpatterns = [
    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup'),
]
