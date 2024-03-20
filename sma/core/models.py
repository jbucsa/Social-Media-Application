from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
# we are creating the profile model here: Aldo Resendiz
# django is gonna give us the username, firstname, lastname, email, and password by default
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username