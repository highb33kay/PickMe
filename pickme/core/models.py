from django.db import models

# create a sex option 


# Create your models here.
# create a user model
class User(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    NONBINARY = 'NB'
    GENDER = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NONBINARY, 'Non-Binary')
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=2,
        choices=GENDER,
        default=FEMALE,
    )


    def __str__(self):
        return self.name
    
# create a pick model
class PickUpLine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    line = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    gender = models.Cha
    # sort by gender

    def __str__(self):
        return self.line
    
    # sort by gender

    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pick = models.ForeignKey(PickUpLine, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

    def __str__(self):
        return self.like

class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pick = models.ForeignKey(PickUpLine, on_delete=models.CASCADE)
    dislike = models.BooleanField(default=False)

    def __str__(self):
        return self.dislike
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pick = models.ForeignKey(PickUpLine, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)

    def __str__(self):
        return self.comment

