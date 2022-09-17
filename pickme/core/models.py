from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify
# create a sex option 

# create a  user profile model
# class Profile(models.Model):
#     pass
    

# # create a user model
class User(AbstractUser):
#    Creating a sex option for the user.
    MALE = 'M'
    FEMALE = 'F'
    NONBINARY = 'NB'
    GENDER = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NONBINARY, 'Non-Binary')
    ]
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=2,
        choices=GENDER,
        default=FEMALE,
    )
    pass

    def __str__(self):
        return self.username
    
# create a pick model
class PickUpLine(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False)
    line = models.CharField(max_length=250)
    likes = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(max_length=200, blank=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    last_edited = models.DateTimeField(auto_now=True, null=True)
    
    # save method
    def save(self, *args, **kwargs):
        self.url = slugify(self.line)
        super(PickUpLine, self).save(*args, **kwargs)

    def __str__(self):
        return self.line
    
    # sort by gender

# preference model for like and dislike
class Preference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pick = models.ForeignKey(PickUpLine, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.user) + "." + str(self.pick) + "." + str(self.value)
    
    class meta:
        unique_together = ('user', 'pick', 'value')
    
# class Like(models.Model):
#     pick = models.ForeignKey(PickUpLine, on_delete=models.CASCADE)
#     like = models.BooleanField(default=False)


#     def __str__(self):
#         return self.like
