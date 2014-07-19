from django.contrib import admin

# Register your models herle.
from dps.models import Users,Orders,DeliverClient
class UsersAdmin(admin.ModelAdmin):#for showing more than one value in Users table
	list_display = ('id','username','first_name','last_name','email')#showing values in table
	search_fields = ('username','first_name','last_name')
	list_filter = ('username','first_name')
	
class OrdersAdmin(admin.ModelAdmin):#for showing more than one value in Orders table
	list_display = ('id','customer','productName','Quantity','contact_no','dest_lat','dest_lng','date_order','deliver_status')
	search_fields = ('id','Quantity')#adding search field to admin panel at table Orders by username,firstname,lastname
	list_filter = ('customer','date_order')
admin.site.register(Users,UsersAdmin)
admin.site.register(Orders,OrdersAdmin)
admin.site.register(DeliverClient)
