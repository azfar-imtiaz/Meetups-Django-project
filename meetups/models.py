from django.db import models

# Create your models here.


# NOTE: Please ensure that 'meetups' was added to INSTALLED_APPS
# in settings.py!

class Meetup(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	description = models.TextField()
	image = models.ImageField(upload_to='images')