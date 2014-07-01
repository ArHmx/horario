from django.db import models

# Create your models here.
class Teacher(models.Model):
	name = models.CharField(max_length=40)

	def __str__(self):
		return '%s' % (self.name)

class Group(models.Model):
	name = models.CharField(max_length=25)

	def __str__(self):
		return '%s' % (self.name)

class Subject(models.Model):
	name = models.CharField(max_length=30)
	Teach_by = models.ForeignKey('Teacher')
	Teaching = models.ForeignKey('Group')

	def __str__(self):
		return '%s' % (self.name)