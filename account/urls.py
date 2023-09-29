from django.urls import path

from . import views

app_name = 'account'
urlpatterns = [
    path('login', views.UserLogin.as_view(), name='user_login'),
    path('otplogin', views.OtpLoginView.as_view(), name='user_otp_login'),
    path('check', views.CheckOtpView.as_view(), name='check_otp'),
    path('logout', views.UserLogout, name='user_logout'),
    path('register', views.RegisterUserView.as_view(), name='user_register'),
    path('add/address', views.AddressView.as_view(), name='add_address'),
]