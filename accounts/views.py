from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse

from auth_module.utilits import verify_turnstile
from .models import CustomUser
from .services import UserService, RoleService
from .utils import validate_password

class RegisterOwnerView(APIView):
    def get(self, request):
        return Response({
            "message": "Bu endpoint faqat POST uchun ishlaydi.",
            "description": "User yaratish uchun telefon raqam, fullname va password yuboring",
            "required_body": {
                "full_name": "Ism Familiya",
                "primary_mobile": "+998901234567",
                "password": "StrongPass@123",
            }
        }, status=status.HTTP_200_OK)

    def post(self, request):

        data = request.data
        password = data.get('password')
        phone_number = data.get('primary_mobile')
        full_name = data.get('full_name')

        validate_password((password))

        user = UserService.register_user(
            full_name=full_name,
            primary_mobile=phone_number,
            password=password
        )
        return Response(
            {"msg":f"{user.username} mufaqiyatli yaratilindi"},
                  status=status.HTTP_201_CREATED
        )


class ChangeUserRoleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        new_role = request.data.get("new_role")
        user = RoleService.change_user_role(request.user, user_id, new_role)
        return  Response({"msg": f"{user.username} role {user.user_role} ga o'zgartirildi"})


class SessionTestAPIView(APIView):
    def get(self, request):
        remaining = request.session.get_expiry_age()  # session qolgan vaqti soniyada
        print(remaining, "vaqt")
        return Response(
            {"session_remaining_seconds": remaining},
            status=status.HTTP_200_OK
        )
