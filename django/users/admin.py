from django.contrib import admin
from .models import Service, BasicService, StandardService, PremiumService
from .models import Arizalar
from .models import User
@admin.register(User)
# Register your models here.
class User(admin.ModelAdmin):
    list_display = ['id','full_name', 'username', 'user_id', 'created_at','updated_at']
    search_fields = ['id','full_name', 'username','user_id']

class ArizalarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'user_id', 'phone_number')
    search_fields = ('name', 'username', 'user_id', 'phone_number')
    list_filter = ('name',)

admin.site.register(Arizalar, ArizalarAdmin)

class BasicServiceInline(admin.StackedInline):
    model = BasicService
    extra = 1

class StandardServiceInline(admin.StackedInline):
    model = StandardService
    extra = 1

class PremiumServiceInline(admin.StackedInline):
    model = PremiumService
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'photo', 'description')
    search_fields = ('fullname',)
    inlines = [BasicServiceInline, StandardServiceInline, PremiumServiceInline]

@admin.register(BasicService)
class BasicServiceAdmin(admin.ModelAdmin):
    list_display = ('iid', 'service', 'description', 'price')
    search_fields = ('service__fullname',)

@admin.register(StandardService)
class StandardServiceAdmin(admin.ModelAdmin):
    list_display = ('iid', 'service', 'description', 'price')
    search_fields = ('service__fullname',)

@admin.register(PremiumService)
class PremiumServiceAdmin(admin.ModelAdmin):
    list_display = ('iid', 'service', 'description', 'price')
    search_fields = ('service__fullname',)
