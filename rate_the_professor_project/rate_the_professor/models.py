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


# Every university will have many departments and every course will belong to a department
class Department(models.Model):
    department_name = models.CharField(max_length=512)
    university = models.ForeignKey(University)

    def __unicode__(self):
        return self.department_name


# Every course is delivered by one university and is taught by many professors
class Course(models.Model):
    course_name = models.CharField(max_length=512)
    university = models.ForeignKey(University)
    department = models.ForeignKey(Department)
    start_date = models.DateField()

    def _course_date(self):
        return self.start_date.strftime("'%Y")
    course_date = property(_course_date)

    def __unicode__(self):
        return u'%s %s' % (self.course_name, self.course_date)


# Every professor will receive many ratings, may teach many modules but works for one university
class Professor(models.Model):
    title = models.CharField(max_length=64)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    # communication
    sum_of_communication = models.DecimalField(max_digits=10, decimal_places=1, default=2.5)
    no_of_communication = models.IntegerField(default=1)
    overall_communication = models.DecimalField(max_digits=2, decimal_places=1, default=2.5)

    #knowledge
    sum_of_knowledge = models.DecimalField(max_digits=10, decimal_places=1, default=2.5)
    no_of_knowledge = models.IntegerField(default=1)
    overall_knowledge = models.DecimalField(max_digits=2, decimal_places=1, default=2.5)

    #approachability
    sum_of_approachability = models.DecimalField(max_digits=10, decimal_places=1, default=2.5)
    no_of_approachability = models.IntegerField(default=1)
    overall_approachability = models.DecimalField(max_digits=2, decimal_places=1, default=2.5)

    #enthusiasm
    sum_of_enthusiasm = models.DecimalField(max_digits=10, decimal_places=1, default=2.5)
    no_of_enthusiasm = models.IntegerField(default=1)
    overall_enthusiasm = models.DecimalField(max_digits=2, decimal_places=1, default=2.5)

    #clarity
    sum_of_clarity = models.DecimalField(max_digits=10, decimal_places=1, default=2.5)
    no_of_clarity = models.IntegerField(default=1)
    overall_clarity = models.DecimalField(max_digits=2, decimal_places=1, default=2.5)

    #awesomeness
    sum_of_awesomeness = models.DecimalField(max_digits=10, decimal_places=1, default=2.5)
    no_of_awesomeness = models.IntegerField(default=1)
    overall_awesomeness = models.DecimalField(max_digits=2, decimal_places=1, default=2.5)

    #overall
    sum_of_ratings = models.DecimalField(max_digits=10, decimal_places=1, default=2.5)
    no_of_ratings = models.IntegerField(default=1)
    overall_rating = models.DecimalField(max_digits=2, decimal_places=1, default=2.5)

    picture = models.ImageField(upload_to='professors', blank=True)
    university = models.ForeignKey(University)
    courses_taught = models.ManyToManyField(Course)
    website_url = models.URLField()

    def _full_name(self):
        return u'%s %s %s ' % (self.title, self.first_name, self.last_name)
    full_name = property(_full_name)

    def __unicode__(self):
        return u'%s %s - %s - ratings: %d overall: %.2f' % (self.first_name, self.last_name, self.university,
                                                            self.no_of_ratings, self.overall_rating)


# Rating table will store all ratings submitted by a user and received by a professor
class Rating(models.Model):
    user = models.ForeignKey(User, null=True)
    professor = models.ForeignKey(Professor)
    communication = models.DecimalField(max_digits=2, decimal_places=1, default=2.5)
    knowledge = models.DecimalField(max_digits=2, decimal_places=1, default=2.5)
    approachability = models.DecimalField(max_digits=2, decimal_places=1, default=2.5)
    enthusiasm = models.DecimalField(max_digits=2, decimal_places=1, default=2.5)
    clarity = models.DecimalField(max_digits=2, decimal_places=1, default=2.5)
    awesomeness = models.DecimalField(max_digits=2, decimal_places=1, default=2.5)
    comment = models.CharField(max_length=1024, null=False)
    # DateField.auto_now
    # Automatically set the field to now every time the object is saved. Useful for last-modified timestamps.
    # Note that the current date is always used its not just a default value that you can override.
    # DateField.auto_now_add
    # Automatically set the field to now when the object is first created. Useful for creation of timestamps.
    # Note that the current date is always used its not just a default value that you can override.
    datetime = models.DateTimeField(auto_now_add=True)

    # Rating will have a calculated property
    def _calculate_rating(self):
        return u'%.2f' % ((self.communication + self.knowledge + self.approachability
                + self.enthusiasm + self.clarity + self.awesomeness) / 6)
    rating = property(_calculate_rating)

    def __unicode__(self):
        return u'%s - %s %s Rating: %.2f - %s' % (self.comment, self.professor.first_name,
                                                  self.professor.last_name, self.rating,
                                                  self.professor.university)
