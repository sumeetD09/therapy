from django.contrib.auth.models import User
from django.db import models

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    remember_me = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
#---------------------------------- questions models--------------------------------



class TherapyQuestionnaire(models.Model):
    q1 = models.TextField(help_text="Why are you seeking therapy?")
    q2 = models.CharField(
        max_length=50, 
        choices=[
            ("Less than 1 month", "Less than 1 month"),
            ("1-6 months", "1-6 months"),
            ("6-12 months", "6-12 months"),
            ("Over a year", "Over a year"),
        ],
        help_text="How long have you been experiencing these issues?"
    )
    q3 = models.CharField(
        max_length=3, 
        choices=[("Yes", "Yes"), ("No", "No")],
        help_text="Have you sought therapy before?"
    )
    q4 = models.TextField(help_text="What are your goals for therapy?")
    q5 = models.CharField(max_length=255, help_text="Preferred days and times for sessions")
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Therapy Questionnaire submitted on {self.submitted_at}"
#------------------------------------------------------------------------login--------------
from django.db import models

class LoginTable(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    remember_me = models.BooleanField(default=False)

    def __str__(self):
        return self.email








#------------------------------------------------------------------------
from django.db import models
from django.core.mail import send_mail
from django.utils import timezone

class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.date} {self.time}"

    def send_notification(self):
        # Sending email notification
        send_mail(
            'Therapy Session Booking Confirmation',
            f'Dear {self.full_name},\n\nYour booking for {self.date} at {self.time} is confirmed.\n\nThank you for choosing our service!',
            'your-email@example.com',  # From email
            [self.email],  # To email
            fail_silently=False,
        )

    def save(self, *args, **kwargs):
        # Send email notification when a booking is created
        if not self.pk:
            self.send_notification()
        super().save(*args, **kwargs)

#333333333333333333333333333333333333333333333333333333333333 

from django.db import models

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('paypal', 'PayPal'),
        ('creditCard', 'Credit Card'),
    ]

    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    paypal_email = models.EmailField(blank=True, null=True)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    card_holder_name = models.CharField(max_length=100, blank=True, null=True)
    expiry_date = models.CharField(max_length=5, blank=True, null=True)
    cvv = models.CharField(max_length=4, blank=True, null=True)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_payment_method_display()} - {self.payment_date.strftime('%Y-%m-%d %H:%M:%S')}"






