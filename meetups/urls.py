from django.urls import path

from . import views

# NOTE: this variable must always be named urlpatterns, and it must be a list
# This list contains a mapping from routes to their corresponding functions
# 	that generate the appropriate view

'''
	NOTE: For any URL that you add here, it is a good idea to add a slash
	after it. This ensures that the URL is hit whether it is followed by 
	a slash or not. For example:
	path('meetups/', views.index) means that "localhost:7000/meetups" and 
	"localhost:7000/meetups/" will both hit the views.index function
'''

urlpatterns = [
	path('meetups/', views.index, name='all-meetups'),
	# specifying the type as slug isn't necessary
	path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-details')
]