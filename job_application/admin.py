from django.contrib import admin
from .models import From


class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "date", "occupation")
    search_fields = ("first_name", "last_name", "email", "date", "occupation")
    list_filter = ("first_name", "last_name", "email", "date", "occupation")
    ordering = ("-first_name", )
    readonly_fields = ("occupation", "date", "email", )

admin.site.register(From, FormAdmin)