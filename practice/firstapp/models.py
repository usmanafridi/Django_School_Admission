from django.db import models

class Admission(models.Model):
	SEX_CHOICES=[('M', 'Male'), ('F','Female')]
	name= models.CharField(max_length=100)
	father_name= models.CharField(max_length=100)
	city= models.CharField(max_length=100, blank=True)
	score= models.CharField(max_length=100)
	sex=models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
	birth_date=models.DateTimeField()
	age=models.IntegerField(null=True)
	vaccinations=models.ManyToManyField('Vaccine', blank=True)
	

class Vaccine(models.Model):
	name=models.CharField(max_length=50)

	def __str__(self):
		return self.name
