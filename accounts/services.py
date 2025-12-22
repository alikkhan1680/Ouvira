from rest_framework.exceptions import PermissionDenied
from .models import CustomUser



class UserService:

    @staticmethod
    def register_user(**data):
        return CustomUser.objects.create_user_with_role(**data)


class RoleService:

    @staticmethod
    def change_user_role(actor_user, target_user_id, new_role):
        target_user = CustomUser.objects.get(id=target_user_id)

        # permission tekshiruvi
        role_hierarchy = {
            "account_owner": 4,
            "admin": 3,
            "manager": 2,
            "employee": 1
        }

        if role_hierarchy.get(actor_user.user_role, 0) <= role_hierarchy.get(target_user.user_role, 0):
            raise PermissionDenied("Siz bu foydalanuvchining ro'lini ozgartira olmaysiz")


        old_role = target_user.user_role
        target_user.user_role = new_role
        target_user.save()

        from .models import RoleChangeLog
        RoleChangeLog.objects.create(
            user=target_user,
            old_role=old_role,
            new_role=new_role,
            changed_by=actor_user
        )

        return target_user
