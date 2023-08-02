from django.contrib import admin

# Register your models here.
from . import models


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'prefix',
        'std_id',
        'first_name',
        'last_name',
        'phone',
    )