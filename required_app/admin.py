from django.contrib import admin

from required_app.models import Engineer, Client, RequiredProject, Segment, SubmittedProject


class RequiredProjectAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'required_id',
        'client',
        'project_name',
        'required_date'
    ]


admin.site.register(Engineer)
admin.site.register(Client)
admin.site.register(RequiredProject, RequiredProjectAdmin)
admin.site.register(Segment)
admin.site.register(SubmittedProject)
