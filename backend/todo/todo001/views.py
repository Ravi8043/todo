from django.shortcuts import render,redirect
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
class todo_list(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class todo_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
