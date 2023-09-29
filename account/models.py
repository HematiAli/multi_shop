from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not phone:
            raise ValueError("Users must have an phone address")

        user = self.model(
            phone=phone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            phone,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="ادرس ایمیل",
        max_length=255,
        unique=True
    )
    fullname = models.CharField(max_length=50, verbose_name='نام و نام خوانوادگی')
    phone = models.CharField(max_length=12, unique=True, verbose_name='شماره تلفن')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False, verbose_name='ادمین')
    image = models.ImageField(upload_to='user-image', null=True, blank=True, verbose_name='عکس پروفایل' )

    objects = UserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Otp(models.Model):
    token = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11, verbose_name="تلفن")
    code = models.SmallIntegerField(verbose_name='کد تایید')
    expiration_data = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انفضل')


    class Meta:
        verbose_name = 'اعتبار سنجی '
        verbose_name_plural = 'اعتبار سنجی ها'


    def __str__(self):
        return self.phone


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=300)
    postal_code = models.CharField(max_length=100)

    def __str__(self):
        return self.user.phone
