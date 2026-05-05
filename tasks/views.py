from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.timezone import now
from .models import Task

class DashboardView(APIView):
    def get(self, request):
        tasks = Task.objects.filter(assigned_to=request.user)

        data = {
            "total": tasks.count(),
            "completed": tasks.filter(status="DONE").count(),
            "pending": tasks.filter(status="TODO").count(),
            "overdue": tasks.filter(due_date__lt=now()).count(),
        }

        return Response(data)