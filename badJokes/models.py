from django.db import models

class Players(models.Model):
	person = models.CharField(max_length=200)
	photo_link = models.CharField(max_length=200,default='http://blog.accupass.com/wp-content/uploads/2017/03/1_120122230539_1.jpg')
	pub_date = models.DateTimeField('date published')
	is_active = models.BooleanField(default=1)
	def __str__(self):
		return self.person

class Badjokes(models.Model):
	players = models.ForeignKey(Players, on_delete=models.CASCADE)
	game_round = models.IntegerField(default=0)	
	scores = models.IntegerField(default=0)    
	pub_date = models.DateTimeField('date published')


# Create your models here.
