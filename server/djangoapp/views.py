from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
from django.shortcuts import render
import logging
import json
from .models import reviews  # Import your Review model
from .models import Dealer  # Import your Dealer model

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Update the `get_dealerships` view
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)

# Update the `get_dealer_details` view
def get_dealer_details(request, dealer_id):
    dealer = get_object_or_404(Dealer, pk=dealer_id)
    reviews = dealer.review_set.all()
    context = {'dealer': dealer, 'reviews': reviews}
    return render(request, 'djangoapp/dealer_details.html', context)

# Update the `add_review` view
def add_review(request, dealer_id):
    dealer = get_object_or_404(Dealer, pk=dealer_id)

    if request.method == 'POST':
        rating = request.POST['rating']
        comment = request.POST['comment']
        Review.objects.create(dealer=dealer, rating=rating, comment=comment)
        messages.success(request, 'Review added successfully.')
        return redirect('djangoapp:get_dealer_details', dealer_id=dealer_id)

    context = {'dealer': dealer}
    return render(request, 'djangoapp/add_review.html', context)

def index(request):
    return render(request, 'djangoapp/index.html')

def about(request):
    context = {}
    return render(request, 'djangoapp/about.html', context)


def contact(request):
    context = {}
    return render(request, 'djangoapp/contact.html', context)


def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('djangoapp:get_dealerships')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'djangoapp/login.html')


def logout_request(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('djangoapp:get_dealerships')


def registration_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        messages.success(request, 'Registration successful. Please log in.')
        return redirect('djangoapp:login_request')
    return render(request, 'djangoapp/registration.html')


# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)




def get_dealer_details(request, dealer_id):
    dealer = get_object_or_404(Dealer, pk=dealer_id)
    # Assuming you have a related model for reviews, adjust accordingly
    reviews = dealer.review_set.all()  
    context = {'dealer': dealer, 'reviews': reviews}
    return render(request, 'djangoapp/dealer_details.html', context)




def add_review(request, dealer_id):
    dealer = get_object_or_404(Dealer, pk=dealer_id)
    
    if request.method == 'POST':
        rating = request.POST['rating']
        comment = request.POST['comment']
        Review.objects.create(dealer=dealer, rating=rating, comment=comment)
        messages.success(request, 'Review added successfully.')
        return redirect('djangoapp:get_dealer_details', dealer_id=dealer_id)

    context = {'dealer': dealer}
    return render(request, 'djangoapp/add_review.html', context)

