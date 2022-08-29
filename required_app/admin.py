from django.contrib import admin

from required_app.models import Engineer, Client, RequiredProject, Segment

admin.site.register(Engineer)
admin.site.register(Client)
admin.site.register(RequiredProject)
admin.site.register(Segment)
