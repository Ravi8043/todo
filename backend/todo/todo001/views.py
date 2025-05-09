from django.shortcuts import render,redirect
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
