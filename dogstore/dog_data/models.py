from django.db import models
import datetime

# Create your models here.

# class contact(models.Model):

#     name=models.CharField( max_length=50)
#     mail=models.CharField(max_length=50)
#     subject=models.CharField(max_length=50)
#     message=models.CharField(max_length=50)


class inquiry(models.Model):

    name=models.CharField( max_length=50)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)

# def __str__(self):
#     return self.name
    
# we are creating the products page now
class category(models.Model):
    name=models.CharField(max_length=50)
     
    def __str__(self):
        return self.name
    
class customer(models.Model):
    first_name=models.CharField( max_length=50)
    last_name=models.CharField( max_length=50)
    phone=models.CharField( max_length=50)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
# class product(models.Model):
#     name=models.CharField( max_length=50)
#     price=models.DecimalField( max_digits=5, decimal_places=2,default=0)
#     category=models.ForeignKey(category, on_delete=models.CASCADE,default=1)
#     description=models.CharField(max_length=50,default=" " , blank=True , null=True)
#     image=models.ImageField( upload_to="uploads/product/")
    
#     def __str__(self):
#         return self.name
    
    
# class order(models.Model):
#     product=models.ForeignKey(product,on_delete=models.CASCADE)
#     customer=models.ForeignKey(customer,on_delete=models.CASCADE)
#     quantity=models.IntegerField(default=1)
#     address=models.CharField(max_length=50,default=" ", blank=True)
#     phone=models.CharField(max_length=50,default=" ", blank=True)
#     date=models.DateField(default=datetime.datetime.today)
#     status=models.BooleanField(default=False)
    
#     def __str__(self):
#         return self.product
    


class addnewpet(models.Model):
    pet_id = models.CharField(max_length=100,primary_key=True)
    name=models.CharField(max_length=50)
    breed=models.CharField(max_length=50)
    sex=models.CharField(max_length=10)
    color=models.CharField(max_length=50)
    image=models.ImageField( upload_to="image/")


    def __str__(self):
        return self.name










