from django.db import models

# Create your models here.

class Clinic(models.Model):
    name=models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Doctor(models.Model):
    name=models.CharField(max_length=100)
    specialty=models.CharField(max_length=100)
    clinic=models.ForeignKey(Clinic,on_delete=models.CASCADE)
    education = models.CharField(max_length=200)
    work_experience = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Queue(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    queue_number = models.PositiveIntegerField()
    
