from django.shortcuts import render
from .models import Book
from .serializers import Bookserializer
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.
class ApiHomePage(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer

class ApiDetailPage(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer
    lookup_field = "id"