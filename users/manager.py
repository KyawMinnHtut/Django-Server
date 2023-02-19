from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password):
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(username=self.username)
        user.set_password(password)
        user.save(using=self._db)
        return user
