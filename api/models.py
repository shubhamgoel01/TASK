from django.db import models

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    age = models.IntegerField() 

    def __str__(self):
        return self.customer_name

class MobileCompany(models.Model):
    company_name = models.CharField(max_length=100) 
    number = models.IntegerField() 
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customer')

    def __str__(self):
        return self.company_name


