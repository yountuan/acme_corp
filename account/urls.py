from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, ActivationView, DeleteAccountView, ObtainActivationCodeView, CustomTokenObtainPairView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('obtain-activation-code/', ObtainActivationCodeView.as_view(), name='obtain-activation-code'),
    path('activate/<str:email>/<str:activation_code>/', ActivationView.as_view(), name='activate'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('delete/<str:email>', DeleteAccountView.as_view(), name='delete_account'),
]
