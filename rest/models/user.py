from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, UserManager
)


class Manager(BaseUserManager):

    def get_by_natural_key(self, email):
        return self.exclude(email__isnull=True).get(**{
            self.model.USERNAME_FIELD: email
        })

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, social_id='',
                    **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if email:
            if User.objects.filter(email=email).count() > 0:
                raise ValueError('Email address already exists')

            user = self.model(email=self.normalize_email(email))
        else:
            raise ValueError('Email address is not set')

        user.is_active = True

        if password:
            user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    objects = Manager()

    USERNAME_FIELD = 'email'

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        null=True
    )

    

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    @staticmethod
    def has_read_permission(request):
        if request.user.is_authenticated:
            if request.user.is_admin or request.user.is_superuser is True:
                return True
            else:
                return False
        else:
            return False

    def has_object_read_permission(self, request):
        return True
      
    @staticmethod
    def has_write_permission(request):
        if request.user.is_authenticated:
            if request.user.is_admin or request.user.is_superuser is True:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def has_update_permission(request):
        if request.user.is_authenticated:
            pk = request.data['id']
            if request.user.is_admin or request.user.is_superuser is True:
                return True
            elif pk == request.user.id:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def has_delete_permission(request):
        return False
