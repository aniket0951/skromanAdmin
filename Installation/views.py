from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse
from rest_framework.generics import *
from rest_framework.mixins import *
from django.contrib import messages
from AdminApp.models import *
from AdminApp.adminserializer import *
from django.views.generic.list import ListView


# Create your views here.
def OpenInstallation(request, tag):
    # context = {'department': 'Installation'}
    if tag == 'installation':
        context = {'department': 'Installation'}
        return render(request, 'InstallationHome.html', context)
    elif tag == 'adduser':
        return redirect('user_list')
    elif tag == 'addNewUser':
        context = {}
        context['department'] = 'Installation'
        context['edit'] = 'addForm'
        return render(request, 'AddNewUser.html', context)    
    else:
        return HttpResponse("no matched tag")

# add new user installation
class InstallationUser(CreateModelMixin, GenericAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def post(self, request , *args, **kwargs):
        add = self.create(request, *args, **kwargs)
        if add:
            messages.success(request, "New User Addedd Successfully.")
            return redirect('user_list')

class InstallationPKClass(UpdateModelMixin, RetrieveModelMixin, GenericAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user_update = self.update(request, *args, **kwargs)
        if user_update:
            messages.success(self.request, "User details updated successfully")
            return redirect('user_list')

    def get(self, request, *args, **kwargs):
        context = {
            'data': self.get_object(),
            'edit': 'edit',
            'department': 'Installation'
        }
        return render(self.request, 'AddNewUser.html', context)

class UserListView(ListView):
    queryset = Users.objects.all().order_by('-id')
    template_name = 'AddNewUser.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['department'] = 'Installation'
        context['edit'] = 'show'
        return context