from django.contrib import admin

from employee import models

# Register your models here.
admin.site.register(models.Employee)
admin.site.register(models.Department)
