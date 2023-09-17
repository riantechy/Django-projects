from django.urls import path
from  profiles.api.views import  profile_check_view,update_profile,profile_check_verified_view

urlpatterns = [
    path('profile/create/',update_profile, name='profile-create'),
    path('profile/', profile_check_view, name='profile-list'),
    path('profile/verify/', profile_check_view, name='profile-verify'),
    
]
