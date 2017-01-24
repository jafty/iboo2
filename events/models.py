from django.db import models
from django.utils import timezone
from django.db.models import Q
from django.shortcuts import render
# Create your models here.
class Event(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	drink = models.BooleanField()
	date = models.DateTimeField()
	password_reg = models.CharField(max_length=50)
	password_acc = models.CharField(max_length=50)
	contact = models.TextField()
	description = models.TextField()
	
	def event_list(request):
		events = Post.objects.all()
		return render(request, 'events/event_list.html', {'events':events})
	
	def event_list(request, pk)
		event = get_object_or_404(Post, pk=pk)
		return render(request, 'blog/event_detail.html', {'post': post})
	
	
		
	
	def __str__(self):
		return self.title
		
		
		
	