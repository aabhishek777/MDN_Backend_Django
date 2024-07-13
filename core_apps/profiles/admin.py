from django.contrib import admin


from core_apps.profiles.models import Profiles



class ProfileAdmin(admin.ModelAdmin):
    list_display= ['pkid', 'id', 'user', 'gender', 'phone_number', 'country','city']
    list_display_links= ['pkid','id','user']
    list_filter= ['id','pkid']
    



admin.site.register(Profiles, ProfileAdmin)
    
# Register your models here.
