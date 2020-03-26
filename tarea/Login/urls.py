from django.urls import include,re_path,path
from django.conf import settings
from.import views
from django.contrib.auth import views as auth_views
# from Login.views import Index
from Login.views import Login_Class
from Login.views import Landing_Class
from Login.views import Dashboard_Class

app_name = 'Login'

urlpatterns = [
    path('', Login_Class.as_view(),name='Login'),
    path('Landing', Landing_Class.as_view(),name='Landing'),
    path('Dashboard/',Dashboard_Class.as_view(),name='Dashboard'),
]