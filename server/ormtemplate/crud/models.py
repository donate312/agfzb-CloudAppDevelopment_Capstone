from django.db import models
from django.utils.timezone import now


class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    car_model = models.ForeignKey('CarModel', on_delete=models.CASCADE)
    review_date = models.DateTimeField(default=now)

    def __str__(self):
        return f"Rating: {self.rating}, Comment: {self.comment}"


class Dealer(models.Model):
    
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=10)
    pass  # Add your fields as needed

class CarMake(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.name} ({self.year.year})"

class CarModel(models.Model):
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    
    def __str__(self):
        return f"{self.make.name} - {self.name} ({self.year})"

    

    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dealer_id = models.IntegerField()  # Assuming dealer_id is an integer, you may need to adjust this
    car_type = models.CharField(max_length=10, choices=CAR_TYPES)
    year = models.DateField()
    

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
        
# Creating a CarMake
make = CarMake.objects.create(name='Toyota', description='Japanese automaker')

# Creating a Dealer
dealer = Dealer.objects.create(name='ABC Motors', address='123 Main St', city='Cityville', state='CA', zip='12345')

# Creating a CarModel
model = CarModel.objects.create(make=make, name='Camry', dealer_id=dealer.id, car_type='SEDAN', year='2023-01-01')

# Creating a Review for the CarModel
review = Review.objects.create(rating=4, comment='Great car!', car_model=model)
