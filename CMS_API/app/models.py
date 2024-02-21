from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)
    full_name = models.CharField(max_length=100)
    phone = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    pincode = models.IntegerField()

    class Meta: 
        managed = True
        db_table = "user_table"
        unique_together = ('email',)

    def save(self, *args, **kwargs): 
        self.username = self.email
        return super().save(*args, **kwargs)
    

    
class ContentItem(models.Model):
    # content_id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contentItem')
    summary = models.CharField(max_length=60, blank=True)
    pdf_file = models.FileField(upload_to='pdfs/')
    category = models.CharField(max_length=20, blank=True)


    def __str__(self):
        return self.author.email
    