from django.contrib import admin
from django.urls import path
from testapp import views
from testapp.views import IndexView
app_name='testapp'

urlpatterns=[
    path('register/',views.get_name,name='get_name'),
    path('login/',views.user_login,name='user_login'),
    path('index/',views.index,name='index'),
    path('form1/',views.college_login,name='college_login'),
    path('user_valid/',views.user_valid,name='user_valid')
    

   

]
