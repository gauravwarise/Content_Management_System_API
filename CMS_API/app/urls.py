from django.urls import path
from .views import *

urlpatterns = [
    path('register', UserRegistrationView.as_view(), name='user_register'),
    path('login', UserLoginView.as_view(), name='user_login'),  
    path('logout', UserLogoutView.as_view(), name='user_logout'),  
    path('getcontent', ContentItems.as_view(), name='getcontent'),  
    path('create', ContentItems.as_view(), name='create'),  
    path('update/<int:pk>/', ContentItems.as_view(), name='update'),  
    path('delete/<int:pk>/', ContentItems.as_view(), name='delete'),  

    # path('delete', DeleteContentView.as_view(), name='delete_content'),
    # path('search', ContentItemSearchView.as_view(), name='content_search'),
    # path('token', CustomAuthToken.as_view(), name='api_token_auth'),


]
