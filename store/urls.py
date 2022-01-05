from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import signup, resend_otp, login_view
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







    path('signup/', signup, name = 'signup'),
	path('login/', login_view, name = 'login'),
	# path('login/', LoginView.as_view(template_name = 'user/login.html', redirect_authenticated_user = True), 
 #    	name = 'login'),
	path('logout/', LogoutView.as_view(next_page = 'login'), name = 'logout'),

	path("password-reset/", 
    	PasswordResetView.as_view(template_name='store/password_reset.html'),
    	name="password_reset"),

	path("password-reset/done/", 
		PasswordResetDoneView.as_view(template_name='store/password_reset_done.html'), 
		name="password_reset_done"),

	path("password-reset-confirm/<uidb64>/<token>/", 
		PasswordResetConfirmView.as_view(template_name='store/password_reset_confirm.html'), 
		name="password_reset_confirm"),

	path("password-reset-complete/", 
		PasswordResetCompleteView.as_view(template_name='store/password_reset_complete.html'), 
		name="password_reset_complete"),

	path('resendOTP', resend_otp),
	# path('followers', followers),
	# path('following', following),
	# path('notifications', notifications),
	# path('notifications/clear', clear_notifications),
	# path('islogin', islogin),


	# path('<str:username>', profile, name='profile'),
	# path('change/<str:fieldname>', ChangeIntoProfile),
]
