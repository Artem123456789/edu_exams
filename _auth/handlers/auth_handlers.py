from django.contrib.auth import get_user_model

from _auth.entities.auth_entities import RegisterInputEntity

User = get_user_model()


class AuthHandler:

    def register(self, input_entity: RegisterInputEntity) -> User:
        user = User(username=input_entity.username)
        user.set_password(input_entity.password)
        user.save()
        return user
