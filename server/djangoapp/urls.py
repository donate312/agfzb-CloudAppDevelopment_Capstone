from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import (
    index,
    get_dealerships,
    get_dealer_details,
    add_review,
    about,
    contact,
    login_request,
    logout_request,
    registration_request,
)

app_name = 'djangoapp'
urlpatterns = [
    path('', views.index, name='index'),  
    path('get_dealerships/', views.get_dealerships, name='get_dealerships'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_request, name='login_request'),
    path('logout/', views.logout_request, name='logout_request'),
    path('registration/', views.registration_request, name='registration_request'),
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='get_dealer_details'),
    path('dealer/<int:dealer_id>/add_review/', views.add_review, name='add_review'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)