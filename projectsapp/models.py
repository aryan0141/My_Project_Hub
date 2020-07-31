from django.db import models

# Create your models here.
class Destination(models.Model):
	projectname = models.CharField(max_length=100)
	category = models.CharField(max_length=100)
	short_desc = models.CharField(max_length=200)
	main_desc = models.TextField()
	upload = models.FileField(blank=True, upload_to='uploads')
	image = models.ImageField(upload_to='pics')
	date =  models.DateField()

	def __str__(self):
		return '{}'.format(self.projectname)
