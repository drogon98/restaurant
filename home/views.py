from django.shortcuts import render,redirect
from django.contrib import messages

from .forms import ReservationForm 

def home(request):
	if request.method == "POST":
		res_form = ReservationForm(request.POST)
		if res_form.is_valid():
			res_form.save()
			messages.success(request,"Thankyou for contacting us.We will get back to you shortly")
			return redirect('home')
	else:
		res_form = ReservationForm()
		return render(request,'index.html',{'r_form':res_form})