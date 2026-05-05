from django.contrib import admin
from django.urls import path, include
from accounts.views import home, signup_page, login_page, dashboard_page
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.views import home, signup_page, login_page, dashboard_page

urlpatterns = [
    path('', home),
    path('signup/', signup_page),
    path('login/', login_page),
    path('dashboard/', dashboard_page),


    path('api/', include('accounts.urls')),
    path('api/', include('tasks.urls')),
    path('api/login/', TokenObtainPairView.as_view()),
]