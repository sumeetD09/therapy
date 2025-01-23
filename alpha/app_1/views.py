from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib import messages
from .models import TherapyQuestionnaire
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import UserProfile,Booking,Payment




#from .forms import SignInForm


# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("Hello, World! This is the Alpha application.")






















def contact(request):
    return HttpResponse(" this is about contact page")

def admindash(request):
    return render(request,'admindash.html')

def individual_T(request):
    return HttpResponse("this is individual sessions page")

def home_p(request):
    return render(request,'index.html')
def faq_p(request):
    return render(request,'faq_p.html')

def doctor_dashboard(request):
    return render (request,'doctor.html')

def admin_dashboard(request):
    return render(request, 'admindash.html')



def therapy_questionnaire_view(request):
    if request.method == "POST":
        q1 = request.POST.get("q1")
        q2 = request.POST.get("q2")
        q3 = request.POST.get("q3")
        q4 = request.POST.get("q4")
        q5 = request.POST.get("q5")

        # Save the data to the database
        TherapyQuestionnaire.objects.create(
            q1=q1,
            q2=q2,
            q3=q3,
            q4=q4,
            q5=q5,
        )

        messages.success(request, "Thank you for submitting the questionnaire!")
        return redirect("your_T")

    return render(request, "questions_p.html")






def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        remember_me = request.POST.get('terms') == 'on'  # Checkbox for 'Terms of Use'

        # Validate form data
        if not email or not password or not repeat_password:
            messages.error(request, 'All fields are required.')
            return render(request, 'sign_up.html')

        if password != repeat_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'sign_up.html')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return render(request, 'sign_up.html')

        # Create the user
        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password),  # Hash the password
        )

        # Create a UserProfile for the user
        UserProfile.objects.create(user=user, remember_me=remember_me)

        # Log the user in after sign-up
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        
        if remember_me:
            request.session.set_expiry(1209600)  # Session expiry for 2 weeks

        messages.success(request, 'Account created successfully!')
        return redirect('questions_p')

    return render(request, 'sign_up.html')


def therapy_registration(request):
    return render(request, "therapy_reg.html") 







def your_T(request):
    return render(request, "your_T.html")



from django.shortcuts import render, redirect
from .models import Booking
from django.contrib import messages

def booking_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full-name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message', '')

        # Save booking to the database
        booking = Booking(
            full_name=full_name,
            email=email,
            phone=phone,
            date=date,
            time=time,
            message=message
        )
        booking.save()
        messages.success(request, 'Your booking has been confirmed!')

        return redirect('payment')

    return render(request, 'booking.html')


from django.shortcuts import render, redirect
from .models import Payment
from django.contrib import messages

from django.shortcuts import render, redirect
from .models import Payment
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def payment_view(request):
    if request.method == 'POST':
        payment_method = request.POST.get('paymentMethod')
        print('Payment method', payment_method)

        # Process PayPal payment
        if payment_method == 'paypal':

            paypal_email = request.POST.get('paypalEmail')
            if not paypal_email:
                messages.error(request, 'PayPal email is required.')
                return redirect('payment')

            # Validate PayPal email
            # try:
            #     validate_email(paypal_email)
            # except ValidationError:
            #     messages.error(request, 'Invalid PayPal email format.')
            #     return redirect('payment')

            # Save PayPal payment to database
            Payment.objects.create(
                payment_method=payment_method,
                paypal_email=paypal_email
            )

        # Process Credit Card payment
        elif payment_method == 'creditCard':
            card_number = request.POST.get('cardNumber')
            card_holder_name = request.POST.get('cardHolderName')
            expiry_date = request.POST.get('expiryDate')
            cvv = request.POST.get('cvv')

            # Validate required fields
            if not all([card_number, card_holder_name, expiry_date, cvv]):
                messages.error(request, 'All credit card fields are required.')
                return redirect('payment')

            # # Basic credit card validation (length, numbers)
            # if len(card_number) not in [13, 16] or not card_number.isdigit():
            #     messages.error(request, 'Invalid card number.')
            #     return redirect('payment')

            # if len(cvv) not in [3, 4] or not cvv.isdigit():
            #     messages.error(request, 'Invalid CVV.')
            #     return redirect('payment')

            # Save Credit Card payment to database
            Payment.objects.create(
                payment_method=payment_method,
                card_number=card_number[-4:],  # Store only the last 4 digits for security
                card_holder_name=card_holder_name,
                expiry_date=expiry_date
            )

        messages.success(request, 'Payment Successful!')
        return redirect('index')

    return render(request, 'payment.html')

def aboutus(request):
    return render(request,'aboutus.html')  

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import LoginTable
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me') is not None

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if remember_me:
                request.session.set_expiry(1209600)  # 2 weeks expiry
            else:
                request.session.set_expiry(0)  # Expires on browser close
            return redirect('index')  # Redirect to homepage after login
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'login.html')
 






