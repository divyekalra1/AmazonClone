from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Product(models.Model):
    name = models.CharField(max_length = 30,blank = False, null = False)
    description = models.TextField(max_length = 200,blank = True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    date_added= models.DateTimeField(auto_now_add=True)
    vendor = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        # count = self.counting()
        return f'{self.vendor}\'s Post '
    # def counting(self):
    #     user = Post.objects.filter(author = f'{self.author}').first()
    #     return user.post_set.count() #user.modelname_set.all() returns the set of all objects of that particular model
