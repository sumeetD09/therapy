

##  **My Therapy Place – Django-Based Mental Health Appointment Portal**

###  **Project Summary:**

*My Therapy Place* is a Django-based web application that allows users to book therapy sessions, fill out pre-session questionnaires, manage user profiles, and securely handle payments through PayPal or credit card. It is designed to streamline mental health support access through a simple, user-friendly interface.

---

###  **Key Features Based on Your Code:**

####  **User Authentication & Profiles**

* Uses Django’s built-in `User` model for authentication.
* Extends the user model with a `UserProfile` that includes a “Remember Me” option for session persistence.

####  **Therapy Questionnaire**

* Collects pre-session data to understand user needs and expectations:

  * Reason for seeking therapy
  * Duration of issues
  * Prior therapy experience
  * Therapy goals
  * Preferred session timings
* Stores submission timestamps for tracking.

####  **Session Booking**

* Allows clients to schedule therapy sessions by providing:

  * Full name, email, phone
  * Desired date and time
  * Optional message
* Sends an **automated email confirmation** upon successful booking.

####  **Payment Handling**

* Supports **PayPal** and **Credit Card** payment options.
* Captures essential payment details like:

  * Email/Card Number
  * Expiry, CVV, Cardholder name
* Automatically records the payment timestamp.

####  **Email Notification System**

* Automatically sends confirmation emails when a booking is created.

---

###  **Tech Stack**

* **Backend:** Python, Django
* **Database:** Default (likely SQLite for development)
* **Frontend:** HTML, CSS (possibly Bootstrap, if used)
* **Email Service:** Django `send_mail()` function
* **Payment Fields:** (Manual entry — no payment gateway integration shown in code)

---



