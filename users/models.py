from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError(_("Email field is required"))
        if not password:
            raise ValueError(_("Password field is required"))
        
        email = self.normalize_email(email=email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_active", True)
        
        user = self.create_user(email, password, **kwargs)
        return user
        
        

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), max_length=255, unique=True,)
    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)
    phone = models.CharField(_("Phone"), max_length=15, blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    
    
    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.name()
     
class BankDetails(models.Model):
    bank_name = models.CharField(_("Bank Name"), max_length=255)
    account_number = models.CharField(_("Account Number"), max_length=255)
    account_name = models.CharField(_("Account Name"), max_length=255)
    
    def __str__(self):
        return f"{self.bank_name} - {self.account_number}"


class HouseAgent(models.Model):
    address = models.CharField(_("Address"), max_length=255)
    NIN = models.CharField(_("NIN"), max_length=255)
    valid_id = models.ImageField(_("Valid ID"), upload_to="house_agent", blank=True, null=True)
    bank_details = models.OneToOneField(BankDetails, on_delete=models.CASCADE, related_name="house_agent")
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="house_agent")
    image = models.ImageField(_("Image"), upload_to="house_agent", blank=True, null=True)
    
    def __str__(self):
        try:
            return f"{self.user.last_name} {self.user.last_name}"
        except:
            return f"{self.NIN}"