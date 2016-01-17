from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Create your models here.



class ViexUserManager(BaseUserManager):

	def create_user(self,email):
		ViexUser.objects.create(email=email)

	def create_superuser(self,email,password):
		self.create_user(email)
		

class ViexUser(AbstractBaseUser,PermissionsMixin):
	email=models.EmailField(primary_key=True)
	USERNAME_FIELD='email'

	objects=ViexUserManager()

	@property 
	def is_staff(self):
		return self.email == 'douglas.jacobson@djunh.com'

	@property
	def is_active(self):
		return True

