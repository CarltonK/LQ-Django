from django.db import models

# Create your models here.
class User(models.Model):
    emailAddress = models.EmailField(max_length = 254)

    def __str__(self):
        return self.emailAddress


