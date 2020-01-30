import json
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from rest_framework.generics import CreateAPIView


# Create your views here.
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(CreateAPIView):
    serializer_class = UserSerializer
    query = User.objects.all()


@csrf_exempt
def add_user_view(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['email']
        first_name = jsonUser['first_name']
        last_name = jsonUser['last_name']
        password = jsonUser['password']
        email = jsonUser['email']
        user_model = User.objects.create_user(username=username, password=password)
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email
        user_model.save()
        return HttpResponse(serializers.serialize("json", [user_model]))
    return render(request,'users/register.html')

@csrf_exempt
def home(request):
    if request.user.is_anonymous:
        return render(request, 'users/login.html')
    return HttpResponseRedirect(reverse('event_list'))



@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        password = jsonUser['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            message = "ok"
        else:
            message = 'Wrong name or password'
        return JsonResponse({"message": message})
    return render(request, 'users/login.html')


