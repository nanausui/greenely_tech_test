from django.contrib import admin
from .models import User, Days, Months

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Days)
class Days(admin.ModelAdmin):
    pass

@admin.register(Months)
class Months(admin.ModelAdmin):
    pass