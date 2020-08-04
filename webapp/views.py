from django.shortcuts import render

# Create your views here.

from .models import Invoice, InvoiceItem, Item
from .serializers import InvoiceSerializer, InvoiceItemSerializer, ItemSerializer
from rest_framework import generics

class InvoiceListCreate(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceItemListCreate(generics.ListCreateAPIView):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer

class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer