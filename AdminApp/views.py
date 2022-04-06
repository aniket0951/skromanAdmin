from django.shortcuts import render, redirect
from common.Helper import *
from .models import *
from .adminserializer import *
from django.contrib import messages
from django.http import *
from SalesApp.views import *
from Installation.views import *

# Create your views here.
# OpenSkroman firstly checks the login user with cookie system, if new user then provides new credentials(cookies) else matches
# with the recorded previous values, this functionality is done via the 1st 3 lines of OpenSkroman func as shown below.
def OpenSkroman(request):
    loginStat = request.COOKIES.get('loginStatus')
    dep = request.COOKIES.get('department')

    email = request.COOKIES.get('email')    # checks the email previously generated.

    if loginStat == "Login" and IsValidParam(dep, request):
        return navigateScreen(request, dep, email)
    else:
        return render(request, 'Login.html')

def LoginUser(request):
    email = request.GET.get('email')
    department = request.GET.get('department')
    otp = request.GET.get('otp')

    # check all params
    if IsValidParam(department, request) and IsValidParam(email, request):

        # check user is register or not
        user = Users.objects.filter(email=email, user_dept=department)
        if department == 'Production' or department == 'Sales' or department == 'Installation':
            return navigateScreen(request, department, email)

        if user:
            otp = generateOTP()
            if SendOTP(email, request, otp):
                login = Users.objects.filter(email=email).update(user_otp=otp)
                loginData = Users.objects.filter(email=email)
                data = UserSerializer(loginData, many=True)

                auth_token = data.data[0]['auth_token']

                messages.info(request, f"{email} {otp}")
                response = render(request, 'Verify.html')
                response.set_cookie('email', email)
                response.set_cookie('sales_user_id', auth_token)
                return response
            else:
                messages.error(request, "Failed to send a verification code please try again.")
                return render(request, 'Login.html')
        else:
            messages.error(request,
                           "Authentication Failed You Are Not A Authenticated User.Please Enter Correct Details")
            return render(request, 'Login.html')
    elif IsValidParam(otp, request):
        return VerifyOtp(request, otp)
    else:
        messages.error(request, "Please enter all details to login.")
        return render(request, 'LoginTemp.html')

# check the department and navigate the screen by dep
def navigateScreen(request, department, email):
    if department == "Admin":
        response = render(request, 'MediaQ.html')
        response.set_cookie('loginStatus', "Login")
        response.set_cookie('department', department)
        return response
    elif department == "Inventory":
        pass
    elif department == 'Production':
        return HttpResponse("Production")
    elif department == 'Sales':
        return OpenUserModes(request, 'openmode')
    elif department == 'Installation':
        user = user_validation(request, "Installation", email)
        if user:
            return OpenInstallation(request,user)
        else:
            messages.error(request, "Unautheraised user. Please provide a authentication details")
            return render(request, "Login.html")     
             
    # elif department == 'Production':
    #     production_user = ProductionUser.objects.filter(emailId=email, department=department)
    #     production_ser = ProductionUserSer(production_user, many=True)

    #     work_for = production_ser.data[0]['work_for']

    #     if production_user:
    #         if work_for == 'Admin':
    #             return redirect('/productionUser/productionHome/')
    #         else:
    #             context = {
    #                 'department': 'ProductionMembers',
    #                 'auth_token': production_ser.data[0]['auth_token']
    #             }
    #             return DailyTasks(request, production_ser.data[0]['auth_token'])

    #     else:
    #         return HttpResponse("Not a production user")

        # all user list show and add new user

