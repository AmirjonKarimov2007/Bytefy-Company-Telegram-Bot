from django.contrib import admin
from .models import User,Services

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'username', 'user_id']  # Customize the fields displayed in the admin interface

# Register your models here.
admin.site.register(User, UserAdmin)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'basic_price','standard_price','premium_price')  # Displayed columns in the admin list view
    search_fields = ('name',)  # Enable searching by name
  # Add filtering by package
    fieldsets = (
        (None, {
            'fields': ('name', 'photo', 'description')
        }),
        ('Package Prices', {
            'fields': ('basic_price', 'standard_price', 'premium_price'),
        }),
    )  # Arrange fields in the admin form

admin.site.register(Services, ServicesAdmin)
