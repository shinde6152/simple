from django.db import models


class admin_login(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


    def get_admin_login_data():
        return admin_login.objects.all()
