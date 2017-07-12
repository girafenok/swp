# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models,connection
from django.contrib.auth.models import User
# Create your models here.

class QuestionManager(models.Manager):
	def new(self):
		pass
	def popular(self):
		pass



class Question(models.Model):
	title=models.CharField(max_length=255)
	text=models.TextField()
	added_at=models.DateTimeField(auto_now_add=True)
	rating=models.IntegerField()
	author=models.ForeignKey(User)
	likes=models.ManyToManyField(User,related_name='question_like_user')
	objects=QuestionManager()

class Answer(models.Model):
	text=models.TextField()
	added_at=models.DateTimeField(auto_now_add=True)
	question=models.ForeignKey('Question')
	author=models.ForeignKey(User)


