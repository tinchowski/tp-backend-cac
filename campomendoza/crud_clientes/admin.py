from django.contrib import admin
from .models import VisitaModel
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")


admin.site.register(VisitaModel)
