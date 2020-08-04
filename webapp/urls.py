from django.urls import path
from . import views

urlpatterns = [
    path('api/invoice/', views.InvoiceListCreate.as_view() ),
    path('api/invoiceitem/', views.InvoiceItemListCreate.as_view() ),
    path('api/item/', views.ItemListCreate.as_view() ),
]