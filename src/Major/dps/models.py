from django.db import models

# Create your models here.
class Users(models.Model):

	#customer_id = models.AutoField("customer_id" ,primary_key=True)
	#customer_id = models.IntegerField("customer_id" ,primary_key=True)
	first_name 	= models.CharField("person's first name", max_length=30)
	last_name 	= models.CharField("person's last name", max_length=30)
	username	= models.CharField("username", max_length=30, unique=True)
	password	= models.CharField("password", max_length=30)
	email		= models.EmailField("person's email address", max_length=75,unique=True)
	phone_number= models.CharField("person's phone number", max_length=30)
	address		= models.CharField("person's address", max_length=30)
	def __unicode__(self):
		return self.username

class Orders(models.Model):
	
    customer = models.ForeignKey(Users)
    contact_no	=models.CharField("contact number of customer", max_length=20,)
    dest_lat 	= models.FloatField("Address latitude", blank=True, default=0.0)
    dest_lng	= models.FloatField("Address longtitude", blank=True, default=0.0)
    productName = models.CharField("product name", max_length=30)
    #order_id    =models.AutoField("order ID",primary_key= True)
    Quantity 	= models.IntegerField("Total Quantity",max_length= 20,default=1)
    deliver_status= models.CharField("deliver status", max_length=30,blank = True,default = "Not delivered")
    date_order	= models.DateField("Date ordered",blank = True,auto_now = True)
    # date_deliver = models.DateTimeField("date delivered",blank =True,auto_now = True)
    def __unicode__(self):
    	return self.productName


class DeliverClient(models.Model):
	deliverboy_id = models.AutoField("deliverboy_id" ,primary_key=True)
	first_name 	= models.CharField("person's first name", max_length=30)
	last_name 	= models.CharField("person's last name", max_length=30)
	username	= models.CharField("username", max_length=30, unique=True)
	password	= models.CharField("password", max_length=30)
	email		= models.EmailField("person's email address", max_length=75,unique=True)
	phone_number= models.IntegerField("person's phone number", max_length=20)
	def __unicode__(self):
		return self.username
    

	

