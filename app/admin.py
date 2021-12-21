from django.contrib import admin

from .models import Client, Contract, Event, Status


class ContractAdmin(admin.ModelAdmin):
    list_display = ("id", "sales", "client_name", "date_updated", "status", "amount", "payment_due",)
    list_filter = ("date_updated",)

    def client_name(self, obj):
        return f"{obj.client.first_name} {obj.client.last_name}"

    def sales(self, obj):
        return f"{obj.sales_contact.username}"


class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "phone", "company", "date_created",)
    list_filter = ("date_created", "date_updated")


class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "client_name", "date_created", "date_updated",)
    list_filter = ("date_created", "date_updated")

    def client_name(self, obj):
        return f"{obj.client.first_name} {obj.client.last_name}"


class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "status",)
    list_filter = ("status",)


admin.site.site_header = "Epic Event Administration"

admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Status, StatusAdmin)
