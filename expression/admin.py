from django.contrib import admin

from .models import InputQuery


class InputQueryAdmin(admin.ModelAdmin):
    fields = ["publeshed_at", "expression"]


admin.site.register(InputQuery, InputQueryAdmin)
