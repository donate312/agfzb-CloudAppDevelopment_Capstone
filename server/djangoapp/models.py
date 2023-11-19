from django.db import models
from django.utils.timezone import now

class reviews(models.Model):
    # Your fields here
    rating = models.IntegerField()
    comment = models.TextField()
    # ... other fields

    def __str__(self):
        return f"Rating: {self.rating}, Comment: {self.comment}"

class Dealer(models.Model):
    # Your Dealer model fields
    pass  # Add your fields as needed

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class CarModel(models.Model):
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more choices as needed
    ]

    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dealer_id = models.IntegerField()  # Assuming dealer_id is an integer, you may need to adjust this
    car_type = models.CharField(max_length=10, choices=CAR_TYPES)
    year = models.DateField()
    # Add other fields as needed

    def __str__(self):
        return f"{self.make} - {self.name} ({self.year.year})"

class CarDealer:
    def __init__(self, dealer_id, name, address, city, state, zip):
        self.dealer_id = dealer_id
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

class DealerReview:
    def __init__(self, dealer_id, name, review, purchase, purchase_date, car_make, car_model, car_year):
        self.dealer_id = dealer_id
        self.name = name
        self.review = review
        self.purchase = purchase
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
