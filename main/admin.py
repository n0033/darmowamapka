from django.contrib import admin
from django.http import HttpResponse
import csv
from main.models import (
    Text,
    User,
    Mail,
    Style
)


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


class TextAdmin(admin.ModelAdmin):
    readonly_fields = ['title']
    list_display = ('title', 'text')


class UserAdmin(admin.ModelAdmin, ExportCsvMixin):
    readonly_fields = ['firstname', 'lastname', 'email', 'phone_number', 'cookie_id', 'video_watched']
    actions = ['export_as_csv']


class MailAdmin(admin.ModelAdmin):
    readonly_fields = ('name',)


admin.site.register(Text, TextAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Mail, MailAdmin)
admin.site.register(Style)
