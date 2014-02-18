from django.db import models
from django.contrib.auth.models import User


# Every university will be unique and will have a website
class University(models.Model):
    name = models.CharField(max_length=256, unique=True)
    url = models.URLField()

    def __unicode__(self):
        return self.name


# UserProfile table extending User model
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    university = models.ForeignKey(University)
    picture = models.ImageField(upload_to='users', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


# Admin table references ids of users who have been given admin rights
class Admin(models.Model):
    user = models.OneToOneField(UserProfile)

    def __unicode__(self):
        return self.user.username


# Every professor will receive many ratings, may teach many modules but works for one university
class Lecturer(models.Model):
    title = models.CharField(max_length=64)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    picture = models.ImageField(upload_to='professors', blank=True)
    fk_university_id = models.ForeignKey(University)
    website = models.URLField()

    def __unicode__(self):
        return self.last_name


# Rating table will store all ratings submitted by a user and received by a professor
class Rating(models.Model):
    fk_user_id = models.ForeignKey(UserProfile)
    fk_lecturer_id = models.ForeignKey(Lecturer)
    communication = models.DecimalField(max_digits=3,decimal_places=2,default=5.00)
    knowledge = models.DecimalField(max_digits=3,decimal_places=2,default=5.00)
    approachability = models.DecimalField(max_digits=3,decimal_places=2,default=5.00)
    enthusiasm = models.DecimalField(max_digits=3,decimal_places=2,default=5.00)
    explaining_material = models.DecimalField(max_digits=3,decimal_places=2,default=5.00)

    # rating will be a calculated field
    def _calculate_rating(self):
        return (self.communication + self.knowledge + self.approachability + self.enthusiasm + self.explaining_material) / 5

    rating = property(_calculate_rating)

    comment = models.CharField(max_length=1024)
    # DateField.auto_now
    # Automatically set the field to now every time the object is saved. Useful for last-modified timestamps.
    # Note that the current date is always used its not just a default value that you can override.
    # DateField.auto_now_add
    # Automatically set the field to now when the object is first created. Useful for creation of timestamps.
    # Note that the current date is always used its not just a default value that you can override.
    datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.user.username


# Every course is delivered by one university and is tought by one lecturer
class Course(models.Model):
    name = models.CharField(max_length=512)
    fk_university_id = models.ForeignKey(University)
    fk_lecturer_id = models.ForeignKey(Lecturer)

    def __unicode__(self):
        return self.name