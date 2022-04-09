import re
from rest_framework import exceptions
import math
import random
from django.core.mail import send_mail
from django.conf import settings
import smtplib
import time
from AdminApp.models import Users
from datetime import datetime, timedelta, date
from dateutil import relativedelta


# -------- to check empty values or null point check -------------
def IsValidParam(param, request):
    if request is not None:
        if not param:
            return False
        else:
            return param, True
    else:
        return exceptions.NotFound("Please provide a validate param")


def SendOTP(email, request, otp):
    htmlgen = f"Your verification code is {otp}"
    send = send_mail('OTP request', otp, email, [
                     email], fail_silently=False, html_message=htmlgen)
    if send:
        return True, otp
    else:
        return False


def GetCurrentTime():
    localtime = time.asctime(time.localtime(time.time()))
    return localtime

# get a random values here


def GenerateRandom(max_length):
    digits = "0123456789"
    value = ""
    for i in range(max_length):
        value += digits[math.floor(random.random() * 10)]
    return value

# get alphnumerical values


def GetAlphNumerical(max_length):
    auth_token = ''.join(random.choice('0123456789ABCDEF')
                         for i in range(max_length))
    return auth_token

# validate user credentials


def user_validation(request, tag, email):
    if tag == "Installation":
        try:
            user = Users.objects.get(email=email, work="installation_user")
            return user
        except Users.DoesNotExist:
            print("user not found")
            return admin_user_validation(request, "Installation", email)

# email validation for admin user


def admin_user_validation(request, tag, email):
    if tag == "Installation":
        try:
            user = Users.objects.get(email=email, work="installation_admin")
            return user
        except Users.DoesNotExist:
            return False

# convert a datetime into date


def get_current_date():
    ts = date.today()
    return ts

def get_current_month():
    month = datetime.now().month
    return month

def get_current_day():
    day = datetime.now().day
    return day

def get_current_year():
    year = datetime.now().year
    return year


def strptime_format_date(input):
    if input:
        return datetime.strptime(str(input), "%Y-%M-%d")


def get_timedelta_compare(date2):
    current_date = get_current_date()
    
    f_date =  date(current_date.year, current_date.month, current_date.day)
    l_date = date(date2.year, date2.month, date2.day)

    delta = abs(l_date - f_date)
    
    pending_days = delta.days

    if l_date == f_date:
        return "Today"
    elif pending_days == 1:
        return "Yesterday"   
    else:
        return f"{pending_days} days ago"
    return None
