from django.contrib import admin
from .models import Invoice, Payment


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'patient', 'total_amount', 'status', 'due_date']
    list_filter = ['status', 'created_at', 'due_date']
    search_fields = ['patient__user__username', 'invoice_number']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'invoice', 'amount', 'payment_date', 'payment_method']
    list_filter = ['payment_method', 'payment_date']
    search_fields = ['invoice__invoice_number']
