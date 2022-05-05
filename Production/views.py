from django.shortcuts import render

# Create your views here.


def Production_Request(request): 
    return render(request, 'ProductionRequest.html')