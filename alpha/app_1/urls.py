from django.contrib import admin
from django.urls import path
from app_1 import views 
from django.urls import path
from . import views











urlpatterns = [
    path('', views.index, name='index'),
    #path('login/', views.user_login, name='login'),
    path('sign_up', views.signup, name='sign_up'),
    path('contact', views.contact, name='contact'),
    path('individual_T', views.individual_T, name='individual_T'),
    path("home_p", views.home_p, name='home_p'),
    path('faq_p', views.faq_p, name='faq_p'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('doctor_dashboard', views.doctor_dashboard, name='doctor_dashboard'),
    path('questions_p', views.therapy_questionnaire_view, name='questions_p'),
    path("your_T", views.your_T, name='your_T'),
   
    path("therapy_registration", views.therapy_registration, name='therapy_registration'),
    
    
    path('payment', views.payment_view, name='payment'),
    




    path('booking/', views.book_session, name='book_session'),


    #path('booking/', views.booking_view, name='booking'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('login/', views.login_view, name='login'),
    
    


    
    
    









    
]




   


