from django.urls import path
from .views import SignUPView, OTPVerifyView, ResentOTPView, LoginView, RefreshTokenView, LogouteView, \
    TwoFAEnableInitiateView, TwoFAEnableVerifyView, Login2FAVerifyView

urlpatterns = [
    path('signup/', SignUPView.as_view(), name='signup'),
    path('verify-otp/', OTPVerifyView.as_view(), name='verify-otp'),
    path("resent-otp/", ResentOTPView.as_view(), name="resent-otp"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogouteView.as_view(), name='logoute'),
    path('tokenrefresh/', RefreshTokenView.as_view(), name='token_refresh'),
    path('2fa-enable-initiate/', TwoFAEnableInitiateView.as_view(), name='2fa-enable-initiate'),
    path('2fa-enable-verify/', TwoFAEnableVerifyView.as_view(), name='2fa-enable-verify'),
    path('login-2fa-verify/', Login2FAVerifyView.as_view(), name='login-2fa-verify'),

]
