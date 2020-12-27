from django.db import models
from django.utils import timezone
# Create your models here.

class post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image = models.ImageField(blank=True,null=True)
    caption = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.caption







# class User_Resistrations(models.Model):  
#     # u_id = models.AutoField(unique=True,primary_key=True) 
#     fname = models.CharField(max_length=100)  
#     lname = models.CharField(max_length=100)  
#     email = models.EmailField()  
#     u_password = models.CharField(max_length=30)  
#     class Meta:  
#         db_table = "User_Resistrations"  
#     def __str__(self):
#         return self.fname+ "  " +self.lname

        