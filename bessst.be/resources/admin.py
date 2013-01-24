from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Resource, ResourceCategory
from wymeditor.admin import RichTextAdmin

class ResourceAdmin(RichTextAdmin):
    pass

admin.site.register(Resource, ResourceAdmin)
admin.site.register(ResourceCategory)

