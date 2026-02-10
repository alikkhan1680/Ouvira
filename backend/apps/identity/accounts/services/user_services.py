from apps.identity.accounts.models import CustomUser
from apps.identity.shared.messages.error import ERROR_MESSAGES
from apps.identity.shared.messages.success import SUCCESS_MESSAGES
from apps.identity.shared.messages.warning import WARNING_MESSAGES


class UserServis:

    @staticmethod
    def update_existing_user(**data):
        primary_mobile = data.get("primary_mobile")
        user = CustomUser.objects.filter(primary_mobile=primary_mobile).first()

        if not user:
            raise ERROR_MESSAGES(ERROR_MESSAGES["ACCOUNT_NOT_FOUND"])

        password = data.pop("password", None)

        for key, value in data.items():
            setattr(user, key,value)

        if password:
            user.set_password(password)

        user.save()
        return user

        """
          Generic helpers
        """
    @staticmethod
    def get_user_by_id(user_id):
        """
        Return user or None
        Used by other module (company, ect.)
        """
        return CustomUser.objects.filter(id=user_id).first()


    @staticmethod
    def has_primary_company(user):
        """
        Safe check
        Works even if field does not ecist yet
        """
        return hasattr(user, "primary_company_id") and bool(user.primary_company_id)


    @staticmethod
    def set_primary_company(*, user_id, company_id):
        """
        set primary company if supported
        Safe for temporary frontent requirements
        """
        user = CustomUser.objects.filter(id=user_id).first()
        if not user:
            raise ERROR_MESSAGES(ERROR_MESSAGES["ACCOUNT_NOT_FOUND"])

        if not hasattr(user, "primary commpany_id"):
            # Temporary: frontend does not need this field yet
            return user

        user.primary_company_id = company_id
        user.save(update_fields=["primary_company_id"])
        return user

