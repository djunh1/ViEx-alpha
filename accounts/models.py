from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
	pass

class User(AbstractBaseUser, PermissionsMixin):

	email = models.EmailField(unique=True, default='test@test.com', primary_key=True)
	username = models.CharField(max_length=40, unique=True, default='test')

	first_name = models.CharField(max_length=40, blank=True)
	last_name = models.CharField(max_length=40, blank=True)
	tagline = models.CharField(max_length=140, blank=True)

	is_staff = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def __unicode__(self):
		return self.username

	def get_full_name(self):
		return ' '.join([self.first_name, self.last_name])

	def get_short_name(self):
		return self.first_name





