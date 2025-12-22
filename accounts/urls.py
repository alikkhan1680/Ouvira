from django.contrib.admin.views.main import ChangeListSearchForm
from django.urls import path
from django.http import JsonResponse
from .views import ChangeUserRoleView, RegisterOwnerView, SessionTestAPIView

def hello_view(request):
    return JsonResponse({"message": "Hello Django!"})

urlpatterns = [
    path('hello/', hello_view, name='hello'),  # http://127.0.0.1:8000/api/accounts/ orqali ishlaydi
    path('user/<int:user_id>/change-role/', ChangeUserRoleView.as_view(), name="change_user_role"),
    path("signup-final/", RegisterOwnerView.as_view(), name="register-owner"),
    path('api/session-test/', SessionTestAPIView.as_view(), name='session-test'),
]
