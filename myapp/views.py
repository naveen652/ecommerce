import random as rand
import pyotp
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Category,Product,Order,UserProfile
# Import your models here

def enter_mobile(request):
    if request.method == 'POST':
        mobile_number = request.POST.get('mobile')

        if mobile_number:
            # Generate a random 6-digit OTP
            otp = str(rand.randint(1000, 9999))

            # Create a TOTP object using the generated OTP

            # Store the OTP in the user's session
            request.session['otp'] = otp

            # Simulate sending the OTP to the user's mobile (replace with your SMS gateway)
            print(f'Sending OTP {otp} to {mobile_number}')

            return JsonResponse({'message': f'OTP sent to {mobile_number}'})
        else:
            return JsonResponse({'message': 'Invalid mobile number'})
    return render(request, 'enter_mobile.html')

def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')

        if entered_otp:
            # Get the stored OTP from the session
            stored_otp = request.session.get('otp')
            print(stored_otp)

            if entered_otp == stored_otp:
                # OTP is verified
                return JsonResponse({'message': 'OTP verified successfully'})
            else:
                # OTP verification failed
                return JsonResponse({'message': 'OTP verification failed'})
    return render(request, 'verify_otp.html')

def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'list_categories.html', {'categories': categories})

def list_products_by_category(request, category_id):
    products = Product.objects.filter(category=category_id)
    return render(request, 'list_products.html', {'products': products})

def place_order(request):
    if request.method == 'POST':
        # Handle order placement here
        return JsonResponse({'message': 'Order placed successfully'})
    return render(request, 'place_order.html')

def my_orders(request):
    orders = Order.objects.filter(user=request.user.userprofile)
    return render(request, 'my_orders.html', {'orders': orders})

def order_details(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'order_details.html', {'order': order})

def profile_details(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'profile_details.html', {'profile': user_profile})

def profile_update(request):
    if request.method == 'POST':
        # Handle profile update here
        return JsonResponse({'message': 'Profile updated successfully'})
    return render(request, 'profile_update.html')
