from django.contrib import admin
from .models import UserProfile, TherapyQuestionnaire, Booking, Payment

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'remember_me')
    search_fields = ('user__username',)
    list_filter = ('remember_me',)

class TherapyQuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('submitted_at', 'q1', 'q2', 'q3', 'q4', 'q5')
    list_filter = ('q2', 'q3', 'submitted_at')
    search_fields = ('q1', 'q4', 'q5')
    ordering = ('-submitted_at',)
    readonly_fields = ('submitted_at',)

    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(TherapyQuestionnaire, TherapyQuestionnaireAdmin)  

class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'date', 'time')
    list_filter = ('date', 'time')
    search_fields = ('full_name', 'email', 'phone', 'message')
    ordering = ('-date', 'time')

admin.site.register(Booking, BookingAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_method', 'paypal_email', 'card_holder_name', 'payment_date')
    list_filter = ('payment_method', 'payment_date')
    search_fields = ('paypal_email', 'card_holder_name', 'payment_method')
    ordering = ('-payment_date',)

admin.site.register(Payment, PaymentAdmin)