from django.urls import path

from .views import (
    create_supplier,
    create_buyer,
    create_product,
    create_order,
    create_delivery,
    SupplierListView,
    BuyerListView,
    ProductListView,
    OrderListView,
    DeliveryListView,
    inventory_view,
    analytics,
    create_bill,
    billList,
    create_employee,
    EmployeeList,
)

urlpatterns = [
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('create-buyer/', create_buyer, name='create-buyer'),
    path('create-product/', create_product, name='create-product'),
    path('create-order/', create_order, name='create-order'),
    path('create-delivery/', create_delivery, name='create-delivery'),

    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
    path('buyer-list/', BuyerListView.as_view(), name='buyer-list'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('delivery-list/', DeliveryListView.as_view(), name='delivery-list'),
    path('inventory-view/', inventory_view, name='inventory-view-list'),
    path('analytics/', analytics, name='analytics'),
    path('create-bill/', create_bill, name='create_bill'),
    path('bill-list/', billList, name='bill-list'),
    path('create-employee/', create_employee, name='create-employee'),
    path('employee-list/', EmployeeList, name='employee-list'),
]
