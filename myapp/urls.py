from django.urls import path
from . import views

app_name = 'myapp'  # Optional, but useful if you have multiple apps

urlpatterns = [
    path('enter_mobile/', views.enter_mobile, name='enter_mobile'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('categories/', views.list_categories, name='list_categories'),
    path('category/<int:category_id>/', views.list_products_by_category, name='list_products_by_category'),
    path('place_order/', views.place_order, name='place_order'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('order/<int:order_id>/', views.order_details, name='order_details'),
    path('profile/', views.profile_details, name='profile_details'),
    path('profile/update/', views.profile_update, name='profile_update'),
]