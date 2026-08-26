from django.contrib import admin

from .models import ContactInquiry


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "inquiry_type",
        "organization",
        "created_at",
        "is_read",
    )
    list_filter = ("inquiry_type", "is_read", "created_at")
    search_fields = ("full_name", "email", "organization", "message")
    readonly_fields = ("created_at",)
    list_editable = ("is_read",)
    date_hierarchy = "created_at"
