from django.contrib import admin

from .models import InputQuery


class InputQueryAdmin(admin.ModelAdmin):
    fields = ["pub_date", "expression"]


admin.site.register(InputQuery, InputQueryAdmin)
