from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from Basic_Authentication_App.models import Employee
from Basic_Authentication_App.api.serializers import EmployeeSerailizer

from rest_framework import viewsets


from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser

class Employee_ModelViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerailizer


    authentication_classes = (SessionAuthentication,)  #for local security these are required with cookies
    permission_classes = (IsAdminUser,)

def login_form_view(request):
    return render(request,'login.html')



def login_user_view(request):  # after entered username and password this url runing
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username,password = password) # may be object or None

    if user is None:
        return redirect("/login/") # redirect to login.html

    else:
        login(request,user)
        return redirect('/api/employees')

def logout_view(request):
    logout(request)
    return redirect("/login/")