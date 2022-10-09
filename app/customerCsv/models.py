from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    registration_date = models.DateTimeField()
    customer_name_kana = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    birth = models.CharField(max_length=200)
    pref = models.CharField(max_length=200)

    def __str__(self):
        return self.customer_id

    def __str__(self):
        return self.customer_name

    def __str__(self):
        return self.registration_date

    def __str__(self):
        return self.email

    def __str__(self):
        return self.gender

    def __str__(self):
        return self.age

    def __str__(self):
        return self.birth

    def __str__(self):
        return self.pref
