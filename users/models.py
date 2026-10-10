import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.validators import FileExtensionValidator
from django.db import models
from django.templatetags.static import static
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class ProfileManager(BaseUserManager):
    def create_superuser(
        self,
        email,
        user_name,
        password,
        first_name="",
        last_name="",
        profile_picture=None,
        **other_fields,
    ):

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")

        return self.create_user(
            email=email,
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
            profile_picture=profile_picture,
            password=password,
            **other_fields,
        )

    def create_user(
        self,
        email,
        user_name,
        password,
        first_name="",
        last_name="",
        profile_picture=None,
        **other_fields,
    ):

        if not email:
            raise ValueError(_("You must provide an email address"))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
            profile_picture=profile_picture,
            **other_fields,
        )
        user.set_password(password)
        user.save()
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_("email address"), unique=True)
    user_name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_("about"), max_length=500, blank=True)
    profile_picture = models.ImageField(
        upload_to="profile_pics/",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=["png", "jpg", "svg"])],
    )
    following = models.ManyToManyField(
        "self", symmetrical=False, blank=True, related_name="followers"
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = ProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_name"]

    @property
    def profile_pic_url(self):
        if self.profile_picture:
            return self.profile_picture.url
        else:
            return static("profile_pics/default_pfp.svg")

    def __str__(self):
        return self.user_name
