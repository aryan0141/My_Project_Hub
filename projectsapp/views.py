#create your views here
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Destination
from django.contrib.auth.models import User, auth
from django.contrib import messages

def index(request):
	if request.method == "POST":
		print(User.is_authenticated)
		if request.user.is_authenticated:
			feedback = request.POST.get("feedback","default")
			check = request.POST.get("check","default")
			print(check)
			print(feedback)
			messages.warning(request,"Your feedback has been submitted.")
			return redirect("/")
		else:
			messages.warning(request,"Login first to send feedback")
			return redirect("login")
	else:
		dests = Destination.objects.all()
		lst = []
		for dest in dests:		
			lst.append(dest)
		return render(request,'index.html', {"lst": lst})

def login(request):
	if request.method == "POST":
		username = request.POST.get("username","default")
		password = request.POST.get("password","default")

		user = auth.authenticate(username = username, password = password)
		if user is not None:
			auth.login(request,user)
			return redirect("/")

		else:
			messages.info(request,"Invalid Credentials!")
			return redirect("login")

	else:	
		return render(request, 'login.html')

def register(request):
	if request.method == "POST":
		fname = request.POST.get("fname","default")
		lname = request.POST.get("lname","default")
		username = request.POST.get("username","default")
		email = request.POST.get("email","default")
		password = request.POST.get("password","default")
		cpassword = request.POST.get("cpassword","default")
		if password==cpassword:
			if User.objects.filter(username = username).exists():
				messages.info(request,"Username already taken!")
				return redirect("register")
			elif User.objects.filter(email = email).exists():
				messages.info(request,"Email already taken!")
				return redirect("register")
			else:
				user = User.objects.create_user(username=username, email=email, password=password, first_name=fname, last_name=lname)
				user.save()
				messages.info(request,"User successfully created!")
				return redirect("/")
		else:
			messages.info(request,"Password not matching!")
			return redirect("register")

	else:
		return render(request, 'register.html')

def logout(request):
	auth.logout(request)
	messages.info(request,"User successfully Logged Out!")
	return redirect('/')

def feedback(request):
	feedback = request.POST.get("feedback","default")
	check = request.POST.get("check","default")
	print(check)
	print(feedback)
	return redirect("/")

def chatter_bot(request):
	if request.user.is_authenticated:
		return render(request, 'chatter_bot.html')
	else:
		messages.info(request,'Login first to see projects.')
		return render(request, 'login.html')