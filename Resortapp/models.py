from django.db import models

# Create your models here.
class Contacts(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=500)
    

sex = [
    ('Male',"Male"),
    ('Female',"Female"),
    ('I rather not say!',"I rather not say!")
]
    
class Members(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    country = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    gender = models.CharField(max_length=20, choices=sex)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
hotels = [
    ('Malika',"Malika"),
    ('Aimi','Aimi'),
    ("Ja'kote","Ja'kote")
]

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=50, choices=hotels)
    location = models.CharField(max_length=50)
    rooms = models.IntegerField()
    workers = models.IntegerField()
    

    def __str__(self):
        return f"{self.hotel_name}"

class dates(models.Model):
    date_booked = models.DateField()
    payment_type = models.CharField(max_length=30)
    status = models.CharField(max_length=50)