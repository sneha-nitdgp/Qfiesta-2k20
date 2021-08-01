from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import datetime


class Profile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	score=models.IntegerField(default=0)
	curr_round=models.IntegerField(default=1)
	submit_time =  models.DateTimeField(auto_now_add=True)
	image=models.TextField(default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRW6X2lldt_gy2tcbXCKBbKWNVBpH-f1Mcjsw&usqp=CAU")

	def __str__(self):
		return self.user.username


	

	
        
@receiver(post_save,sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	#response = kwargs['response']
	#backend = kwargs['backend']
	if created:
		Profile.objects.create(user=instance)
    #if created:
		#response = kwargs['response']

     #   Profile.objects.create(user=instance,image= response['picture'])

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Question(models.Model):
	question=models.CharField(max_length=500)
	ans=models.CharField(max_length=500,default=None)
	round=models.IntegerField(default=1)
	question_type=(
		('audio','audio'),
		('video','video'),
		('image','image'),
		('none','none'),

	)
	my_field=models.CharField(max_length=10, choices=question_type, null='true')
	
	

	def __str__(self):
		return self.question

class Video(models.Model):
	Question=models.OneToOneField(Question, on_delete=models.CASCADE)
	content= models.FileField(upload_to='videos/')
	#video_field=models.BooleanField(default=False)




class Image(models.Model):
	Question=models.OneToOneField(Question, on_delete=models.CASCADE)
	content=models.ImageField(upload_to='images/')
	#image_field=models.BooleanField(default=False)

class Audio(models.Model):
	Question=models.OneToOneField(Question, on_delete=models.CASCADE)
	track=models.FileField(upload_to='audio/')
	#audio_field=models.BooleanField(default=False)


