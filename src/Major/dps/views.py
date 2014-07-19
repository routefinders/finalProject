from django.http import *#for HttpResponse
from django.core.mail import send_mail#for sending mail
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from dps.models import *
from django.core import serializers
#from django.db import connection
from validation import *
#import sqlite3
import pickle
def landing(request):
	return render_to_response('index.html')#'logged_out': '1',}, context_instance=RequestContext(request))
def contactus(request):
	#return render_to_response('contactus.html')#'logged_out': '1',}, context_instance=RequestContext(request))
	errors = []
	if request.method == 'POST':
		if not request.POST.get('subject', ''):
			errors.append('Enter a subject.')
		if not request.POST.get('message', ''):
			errors.append('Enter a message.')
		if not request.POST.get('email') or '@' not in request.POST['email']:
			errors.append('Enter a valid e-mail address.')
		if not errors:
			
			send_mail(request.POST['subject'],request.POST['message'],request.POST.get('email', 'sentiraut@gmail.com'),['aryalprakash.com.np'],fail_silently=False)
			print 'HELLO DIEELKLKE'#throwing erros
			return HttpResponseRedirect('/contact_us/thanks')
			
	return render(request, 'contactus.html',{'errors': errors,'subject': request.POST.get('subject', ''),
		'message': request.POST.get('message', ''),
		'email': request.POST.get('email',''),
		},context_instance=RequestContext(request))

def TakeForm(request):
	user =request.session['user']
	errors =[]
	if request.method == "POST":
		if not request.POST.get('contact', ''):   # first name
			errors.append('Enter a contact number. ')
		if not request.POST.get('product', ''):   # first name
			errors.append('Enter a Product ')
		if not request.POST.get('quantity', ''):   # first name
			errors.append('Enter a Quantity. ')
		if not request.POST.get('latlng', ''):   # first name
			errors.append('Enter a latlng number. ')
		if not errors:
			contact = request.POST.get('contact','')
			product = request.POST.get('product','')
			quantity = request.POST.get('quantity','')
			latlng = request.POST.get('latlng','')
			latlng=latlng.replace('(','')
			latlng=latlng.replace(')','')
			lat,lng = latlng.split(',')
			print (lat,lng,contact,product)
		
			user= Users.objects.filter(id=request.session['id'])
			print user[0]
			print type(user[0])

		
	
			order = Orders(customer=user[0],contact_no = contact, dest_lat=float(lat), dest_lng=float(lng),productName=product,Quantity=int(quantity if quantity else 1),deliver_status="not delivered")
			order.save()
	
	return render(request, 'form.html',{'errors':errors,'contact': request.POST.get('contact',''),'product' : request.POST.get('product',''),
	'quantity' : request.POST.get('quantity',''),
	'latlng' : request.POST.get('latlng','')},
	context_instance=RequestContext(request))
	
def to_json(request):#models to json
	
	tojson= serializers.serialize('json',Orders.objects.all())
	#tojson= serializers.serialize('json',var)
	print tojson
	pickle.dump(tojson,open('orders_json','wb'))
	return HttpResponse(tojson,content_type='json')
def  toKmeans(request):
	values="" 
	value=Orders.objects.all()
	# s=Orders.objects.values('dest_lat','dest_lng')#takiing only dest_lat and dest_lng from db
	# #print s
	
	valuep={}
	
	# #values=Orders.objects.filter()
	# for i in range(0,len(value)):
		 # valuep[i]=(value[i].dest_lat,value[i].dest_lng)
	# #print valuep# to print value from 
	# #print len(valuep)#to check row in databasse
	#pickle.dump(valuep,open('to_prakash.txt','w'))
	orders_dict = {}
	for i in value:
		 orders_dict[ i.customer_id] = i.customer_id,i.customer ,i.dest_lat,i.dest_lng,i.Quantity
		 #valuep[i]=i.dest_lat,i.dest_lng
	# #print orders_dict
		# #print i.Quantity
	pickle.dump(orders_dict,open('orders_dict','wb'))
	# #print orders_dict
	html = "<html><title>from mysql to db</title><body>"
	for i in value:
		html +='''customer = %s &nbsp;customer_id =%s &nbsp<b>lat</b> =%s &nbsp;&nbsp <b>lon</b> =%s &nbsp; &nbsp; Quantity =%s </br>'''%(i.customer,i.customer_id,i.dest_lat,i.dest_lng,i.Quantity)
		values+='''%s	%s \n'''%(i.dest_lat,i.dest_lng)
	
	fh =open("nabin.txt", "w")
	fh.write(values)
	fh.close()
	print values
#print i.Quantity
		
	html+="</body></html>"
	return HttpResponse(html)
	
	 
# def get_lonlat(request):
	# #conn = MySQLdb.connect('localhost','root','','test')
	# conn = sqlite3.connect('database.sqlite3')
	# cursor = conn.cursor()
	# #query = """INSERT INTO `markers`(`id`, `name`, `address`, `lat`, `lng`, `type`) VALUES (%s,%s,%s,%s,%s,%s)"""
	# #querylist = [3300,name,'pulchowk',23.55,55.33,'zpt']
	# #cursor.execute(query,querylist)
	# #value = "SELECT dest_lat,dest_lng FROM orders ORDER BY customer_id"
	# value = "SELECT * FROM orders"
	# cursor.execute(value)
	# html = "<html><title>from mysql to db</title><body>"
	# for row in cursor.fetchall():
		# html +='''
		# <b>lat</b> =%s &nbsp;&nbsp <b>lon</b> =%s</br>'''%(row[0],row[1])
def login(request):
    if request.method=='POST':
        error = ''
        username = request.POST.get('uname')
        password = request.POST.get('password')

        if not username or not password:
            error = 'Both fields must be filled'
        if error:
            return render(request,"login.html",{'error':error})

        user = Validate(username, password)
	
        if user:
            request.session['user'] = user.username

            request.session['id']= user.id
            #print request.session['id']=user.username.id
            return HttpResponseRedirect('/dps/form')
        else:
            error = 'Username/Password do not match'
        if error:
            return render(request,"login.html",{'error':error})
		
			#return HttpResponse("Login Successful!!")

    elif request.method == 'GET':
        return render(request, "login.html")
		

	# # if $POST:
	# # 	nme = $POST['name']
	# html+="</body></html>"
	# #print value.markers.put()
	# return HttpResponse(html)
def logout(request):
    del request.session['user']
    return HttpResponseRedirect('/')	
def signup(request):
    if request.method == 'POST':

        error = ''

        # get all the fields
        fname = request.POST.get('fname', '')   # first name
        lname = request.POST.get('lname', '')   # last name
        uname = request.POST.get('uname', '')   # user name
        password = request.POST.get('password', '')
        cpassword = request.POST.get('cpassword', '')
        address = request.POST.get('address', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        

        # Basic validation
        if not fname or not lname or not uname or not password or not address or not email or not phone  or not cpassword:
            # generate error
            error = " All Fields  are compulsory"
			#return render(request, 'signup.html',{'error':error,'fname': request.POST.get('fname',''),'lname' : request.POST.get('lname',''),
			#'uname' : request.POST.get('uname',''),'password' : request.POST.get('password',''),'email' : request.POST.get('email',''),
			#'phone' : request.POST.get('phone','')}

        #interest_list = interests.split(';')
        #interest_obj_list = []

        # Check if the username/email exists on the system
        if UserExists(uname):
            error = "Username already exists"

        elif EmailExists(email):
            error = "Email already exists"

        elif password != cpassword:
            error = "Passwords do not match"
			#else:

        if error:
            # generate some error message here
            #return HttpResponse(error)
			return render(request,"signup.html",{'error':error})
        else:
			a = Users(username=uname, first_name = fname, last_name=lname, password=password, address=address,email = email, phone_number=phone)
			a.save()
			#user = request.session.get['user']
			return HttpResponse("Sign up was successful ")
		

    elif request.method=='GET':
		#
        return render(request,"signup.html")
