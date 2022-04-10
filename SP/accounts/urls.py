from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.log_in, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('account/', views.accountSettings, name="account"),

    path('', views.home, name="home"),
    path('user/', views.userPage, name="user-page"),
    path('customers/<str:pk_test>/', views.customers, name="customers"),
    path('products/', views.products, name="products"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
        name="password_reset_complete"),


]


