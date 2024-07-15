from django.contrib import admin
from django.utils.html import format_html
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'last_name',
                    'first_name',
                    'group',
                    'flow',
                    'seminarist',
                    'checker',
                    'show_telegram',
                    ]

    @admin.display(description="telegram")
    def show_telegram(self, obj):
        return format_html("<a href='{url}'>Ссылка</a>", url=obj.telegram)

    list_filter = ['checker', 'group', 'seminarist',]
    list_editable = ('checker', 'seminarist', 'flow')
    search_fields = ['last_name', 'first_name',]
