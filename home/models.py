from django.db import models


class Reservation(models.Model):
	full_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=254 ,blank=True)
	phone = models.CharField(max_length=20)
	to_reserve = models.CharField('What should we reserve for you? eg room,table etc',max_length=200)

	def __str__(self):
		return self.full_name


# class Contact(models.Model):
# 	email = models.EmailField(max_length=254)
# 	enquiry = models.TextField()