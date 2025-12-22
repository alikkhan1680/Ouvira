from distutils.sysconfig import customize_compiler

from rest_framework import serializers
from django.core.validators import RegexValidator

from accounts.models import CustomUser
from .models import OTP

class SignUpSerializers(serializers.Serializer):
    full_name = serializers.CharField(max_length=255, allow_blank=False)
    primary_mobile = serializers.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+\d{9,15}$',
                message="telefon raqam + country formatida bo'lishii kerak"
            )
        ]
    )


class OTPVerifyserializers(serializers.Serializer):
    primary_mobile = serializers.CharField(max_length=20)
    otp_code = serializers.CharField(max_length=6)

    def validate(self, data):
        phone = data.get(('primary_mobile'))
        otp = data.get(('otp_code'))

        try:
            otp_obj = OTP.objects.get(phone_number=phone, otp_code=otp)
        except OTP.DoesNotExist:
            raise serializers.ValidationError("OTP expired, please request a new one")

        return data


class ResentOTPSerializers(serializers.Serializer):
    primary_mobile = serializers.CharField(
        validators=[
            RegexValidator(
                regex=r'^\+\d{9,15}$',
                message="telefon raqam + country formatida bo'lishi kerak "
            )
        ]
    )


class LoginSerializer(serializers.Serializer):
    username_or_phone = serializers.CharField()
    password = serializers.CharField(write_only=True)
    remember_me = serializers.BooleanField(default=False)

    def validate(self, attrs):
        username_or_phone = attrs.get('username_or_phone')
        password = attrs.get('password')
        remember_me = attrs.get('remember_me')

        user = None
        if '@' in username_or_phone:
            try:
                user = CustomUser.objects.get(email=username_or_phone)
            except CustomUser.DoesNotExist:
                pass
        else:
            try:
                user = CustomUser.objects.get(primary_mobile=username_or_phone)
            except CustomUser.DoesNotExist:
                pass

        if user and user.check_password(password):
            attrs['user'] = user
            attrs['remember_me'] = remember_me
            return attrs
        raise serializers.ValidationError("Email/Phone yokiy noto'g'ri")


class TwoFAInitiateSerializers(serializers.Serializer):
    qr_url = serializers.CharField(read_only=True)
    secret = serializers.CharField(read_only=True)


class TwoFAVerifySerializer(serializers.Serializer):
    code = serializers.CharField()








