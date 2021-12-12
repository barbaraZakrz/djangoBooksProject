# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# class Another(View):
#
#     books = Book.objects.all()
#     output = ''
#     for book in books:
#         output += f"We have {book.title} book with ID {book.id} <br>"
#
#
#
#     def get( self, request):
#         return HttpResponse(self.output)
#
# def first(request):
#     return HttpResponse('First message from views')

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)