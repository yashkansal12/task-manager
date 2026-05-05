from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SignupSerializer

class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "User created"})
        return Response(serializer.errors)





def home(request):
    return render(request, 'home.html')

def signup_page(request):
    return render(request, 'signup.html')

def login_page(request):
    return render(request, 'login.html')

def dashboard_page(request):
    return render(request, 'dashboard.html')