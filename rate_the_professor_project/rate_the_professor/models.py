from django.db import models
from django.contrib.auth.models import User


# Every university will be unique and will have a website
class University(models.Model):
    uni_name = models.CharField(max_length=256, unique=True)
    website_url = models.URLField()

    def __unicode__(self):
        return self.uni_name


# UserProfile table extending User model
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    fk_university_id = models.ForeignKey(University)
    picture = models.ImageField(upload_to='users', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


# Admin table references ids of users who have been given admin rights
class Admin(models.Model):
    fk_user_id = models.OneToOneField(UserProfile)

    def __unicode__(self):
        return self.user.username


# Every professor will receive many ratings, may teach many modules but works for one university
class Professor(models.Model):
    title = models.CharField(max_length=64)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    rating = models.DecimalField(default=2.5)
    no_of_ratings = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='professors', blank=True)
    fk_university_id = models.ForeignKey(University)
    website_url = models.URLField()

    def __unicode__(self):
        return self.last_name


# Rating table will store all ratings submitted by a user and received by a professor
class Rating(models.Model):
    fk_user_id = models.ForeignKey(UserProfile)
    fk_professor_id = models.ForeignKey(Professor)
    communication = models.DecimalField(max_digits=2,decimal_places=1,default=2.5)
    knowledge = models.DecimalField(max_digits=2,decimal_places=1,default=2.5)
    approachability = models.DecimalField(max_digits=2,decimal_places=1,default=2.5)
    enthusiasm = models.DecimalField(max_digits=2,decimal_places=1,default=2.5)
    clarity = models.DecimalField(max_digits=2,decimal_places=1,default=2.5)
    fun = models.DecimalField(max_digits=2,decimal_places=1,default=2.5)

    # rating will be a calculated field
    def _calculate_rating(self):
        return (self.communication + self.knowledge + self.approachability
                + self.enthusiasm + self.clarity + self.fun) / 6

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
        return self.rating


# Every course is delivered by one university and is taught by many professors
class Course(models.Model):
    course_name = models.CharField(max_length=512)
    start_date = models.DateField
    fk_university_id = models.ForeignKey(University)
    fk_department_id = models.ForeignKey(Department)
    fk_professor_id = models.ManyToManyField(Professor)

    def __unicode__(self):
        return self.course_name


# Every university will have many departments and every course will belong to a department
class Department(models.Model):
    department_name = models.CharField(max_length=512)
    fk_university_id = models.ForeignKey(University)

    def __unicode__(self):
        return self.department_name