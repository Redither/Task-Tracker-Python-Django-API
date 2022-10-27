from django.contrib import admin
from .models import Tasks, Employer, Group
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin

@admin.register(Tasks)
class tasks(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Group)
class group(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
        
@admin.register(Employer)
class employer(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
