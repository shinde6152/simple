from django.db import models

class category(models.Model):
    CATEGORY=models.CharField(max_length=30)


    def __str__(self):
        return self.CATEGORY