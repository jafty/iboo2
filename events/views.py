from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Event
from django.contrib.auth.models import User
from .forms import PassForm, RegistrationForm, EventForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events':events})
   
@login_required
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event':event})

@login_required
def enter_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = PassForm(request.POST or None)
    if request.method == "POST":
        
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == event.password_reg: 
                return render(request, 'events/event_payment.html')
            else:
                events = Event.objects.all()
                return render(request, 'events/event_list.html',{'events':events})

		
			
			
    return render(request, 'events/enter_event.html', {'form': form})

def register(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
			username=form.cleaned_data['username'],
			password=form.cleaned_data['password1'],
			email=form.cleaned_data['email']
			)
			events = Event.objects.all()
			return render(request, 'events/event_list.html', {'events':events})
	else:
		form = RegistrationForm()
	return render(request, 'events/register.html', {'form':form})

@login_required
def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return render(request, 'events/event_detail.html', {'event':event})
    else:
        form = EventForm()
    return render(request, 'events/event_new.html', {'form':form})
			

	


