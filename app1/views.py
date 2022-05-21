from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import json
from app1.models import Choice
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

# Create your views here.
def view1(request, *args, **kwargs):
    return HttpResponse("asdasd")


def create_user(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    else:
        user = User.objects.create_user(request.POST['name'], request.POST['username'], request.POST['password'])
        user.save()
        return HttpResponse('user created')

def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("logged in")
        else:
            return HttpResponse("error log in")

def logout_view(request):
    logout(request)
    return HttpResponse('logged out')

def check_status(request):
    return HttpResponse(f"username: {request.user.username}, {request.user.is_authenticated}")

class SampleClassView(View):

    def post(self, request):
        return HttpResponse(request.read())

    def get(self, requset):
        all_results = Choice.objects.all()
        return HttpResponse(json.dumps(list(all_results.values())))

