from django.contrib import admin
from .models import *

from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class ProfileAdmin(admin.StackedInline):
    model = Profile
    con_delete = False


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileAdmin,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Tag)
admin.site.register(Input)
admin.site.register(Tour)
admin.site.register(Restaurant)
admin.site.register(Stay)
admin.site.register(Schedule)
