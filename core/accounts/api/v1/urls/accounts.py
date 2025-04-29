from django.urls import path,include
from .. import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    # registration
    path('registrations/',views.RegistrationApiView.as_view(),name='registrations'),
    
    path('test-email',views.TestEmailSend.as_view(),name='test-email'),
    # activate
    
    # resend activation
    
    # change password
    path('change-password/',views.changePasswordApiView.as_view(),name='change-password'),
    
    
    # reset password
    
    # login token
    path('token/login/',views.CustomObtainAuthToken.as_view(),name='token-login'),
    path('token/logout/',views.CustomDiscardAuthToken.as_view(),name='token-logout'),
    
    
    # login jwt
    path('jwt/create/',views.CustomTokenObtainPairView.as_view(),name='jwt-create'),
    path('jwt/refresh/',TokenRefreshView.as_view(),name='jwt-refresh'),
    path('jwt/verify/',TokenVerifyView.as_view(),name='jwt-verify'),
    
]