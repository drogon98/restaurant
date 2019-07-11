from django.shortcuts import render,redirect

from .forms import ReservationForm 

def home(request):
	if request.method == "POST":
		res_form = ReservationForm(request.POST)
		if res_form.is_valid():
			res_form.save()
			return redirect('home')
	else:
		res_form = ReservationForm()
		return render(request,'index.html',{'r_form':res_form})