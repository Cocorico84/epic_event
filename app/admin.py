from django.contrib import admin

from .models import Client, Contract, Event, Status


class ClientAdmin(admin.ModelAdmin):
    list_display = ()


class ContractAdmin(admin.ModelAdmin):
    list_display = ("id", "sales_contact", "client_name", "date_updated", "status", "amount", "payment_due",)
    list_filter = ("date_updated", "amount",)

    def client_name(self, obj):
        return f"{obj.client.first_name} {obj.client.last_name}"


admin.site.site_header = "Epic Event Administration"

admin.site.register(Client)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Event)
admin.site.register(Status)
