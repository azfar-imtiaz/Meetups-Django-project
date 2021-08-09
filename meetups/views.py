from django.shortcuts import render
# from django.http import HttpResponse

from .models import Meetup

# Create your views here.

def index(request):
	# return HttpResponse('Hello world!')
	'''
		NOTE: Important: The path to the HTML template is
		from INSIDE the templates folder. So it isn't 
		"templates/meetups/index.html", but rather, it is
		"meetups/index.html"
	'''
	# meetups = [
	# 	{
	# 		'title': 'A first meetup', 
	# 		'location': 'New York', 
	# 		'slug': 'a-first-meetup'
	# 	},
	# 	{
	# 		'title': 'A second meetup', 
	# 		'location': 'San Fransisco', 
	# 		'slug': 'a-second-meeting'
	# 	},
	# ]
	meetups = Meetup.objects.all()
	return render(request, 'meetups/index.html', {
		'show_meetups': True,
		'meetups': meetups
	})

def meetup_details(request, meetup_slug):
	# selected_meetup = {
	# 	'title': 'A first meetup',
	# 	'description': "This is the first meeting"
	# }
	try:
		selected_meetup = Meetup.objects.get(slug=meetup_slug)
		return render(request, 
			'meetups/meetup-details.html', 
			{
				'meetup_found': True,
				'title': selected_meetup.title,
				'description': selected_meetup.description,
				'image': selected_meetup.image.url
			})
	except Exception as e:
		return render(request, 'meetups/meetup-details.html', {'meetup_found': False})