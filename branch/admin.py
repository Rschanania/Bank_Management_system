from django.contrib import admin
from . models import branches,banks
from import_export.admin import ImportExportModelAdmin


@admin.register(branches,banks)
class ViewAdmin(ImportExportModelAdmin):
    pass
