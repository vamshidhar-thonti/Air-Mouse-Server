from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    url = models.TextField()
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE) # Points to the other DB and fetches the id of that user

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200] + "..."

    def pub_date_pretty(self):
        return self.pub_date.strftime('%d %b, %Y')
