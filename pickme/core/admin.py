from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, PickUpLine

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'email']
    

admin.site.register(User, CustomUserAdmin)

# register pickup line model
class PickUpLineAdmin(admin.ModelAdmin):
    list_display = ('line', 'likes')
    list_filter = ('likes',)
    search_fields = ('line',)
    ordering = ('likes',)
    
admin.site.register(PickUpLine, PickUpLineAdmin)