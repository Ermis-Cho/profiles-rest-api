from django.db import models

# Used for overriding or customizing the default Django user model officially
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("Users must have an email address")

        # Converts in lowercase the 2nd half of an email
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

    def del_user(request, username):
        try:
            u = User.objects.get(username=username)
            u.delete()
            messages.success(request, "The user is deleted")

        except User.DoesNotExist:
            messages.error(request, "User doesnot exist")
            return render(request, 'front.html')

        except Exception as e:
            return render(request, 'front.html', {'err': e.message})

        return render(request, 'front.html')


# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # model manager for the objects
    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    # because we are defining a function in a class,
    # we must specify self as the first argument this is the default Python convention

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Return the model as a string"""
        return self.status_text
