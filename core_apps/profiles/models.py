




from django.db import models

from django.contrib.auth import get_user_model
from core_apps.common.models import TimeStampedModel
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


User= get_user_model()


class Profiles(TimeStampedModel):
    class Gender(models.TextChoices):
        MALE= "M",_("Male")
        FEMALE= "F", _("Female")
        OTHERS= "O", _("Other")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number= PhoneNumberField(verbose_name=_("Phone Number"), max_length=30, default="+91 1234567899")
    about_me= models.TextField(verbose_name=_("About me"), default="I am ...")
    gender= models.CharField(verbose_name=_("Gender"),choices=Gender.choices, default=Gender.OTHERS, max_length=20)
    country= CountryField(verbose_name=_("Country Name"), default="IN",null=False)
    city= models.CharField(verbose_name=_("City Name"), default="Delhi", blank=False, null=False)
    profile_photo= models.ImageField(verbose_name=_("Profile Photo"), default="/profile_default.png")
    twitter_handel=models.CharField(verbose_name=_("Twitter"), max_length=40, blank=True)
    followers= models.ManyToManyField("self", symmetrical=False, related_name="following", blank=True)
    
    def __str__(self):
        return  f"${self.user.first_name}'s profile."
    
    def follow(self, profile):
        self.followers.add(profile)
    
    def unfollow(self, profile):
        self.followers.remove(profile)
    
    def check_following(self, profile):
        return self.followers.filter(pkid=profile.pkid).exists()
    
    
    
