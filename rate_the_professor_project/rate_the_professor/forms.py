from django import forms
from rate_the_professor.models import Rating, Professor, UserProfile, Course
from django.contrib.auth.models import User

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('university', 'picture')


class RatingForm(forms.ModelForm):
    communication = forms.DecimalField(initial=2.5)
    knowledge = forms.DecimalField(initial=2.5)
    approachability = forms.DecimalField(initial=2.5)
    enthusiasm = forms.DecimalField(initial=2.5)
    clarity = forms.DecimalField(initial=2.5)
    awesomeness = forms.DecimalField(max_digits=2, decimal_places=1,initial=2.5)
    comment = forms.CharField(widget=forms.TextInput(), max_length=1024, help_text="Please enter the comment here.")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Rating
        fields = ('communication', 'knowledge', 'approachability', 'enthusiasm', 'clarity', 'awesomeness', 'comment')


class ProfessorForm(forms.ModelForm):
    title = forms.CharField(max_length=64, help_text="Title")
    first_name = forms.CharField(max_length=256, help_text="First Name")
    last_name = forms.CharField(max_length=256, help_text="Last Name")

    #courses_thought = Course.objects.filter()
    #fk_courses_taught = models.ManyToManyField(Course)

    #picture = https://docs.djangoproject.com/en/dev/ref/forms/api/#binding-uploaded-files
    website_url = forms.URLField(max_length=200, help_text="Website URL")

    class Meta:
        model = Professor
        fields = ('title', 'first_name', 'last_name', 'website_url', 'university', 'picture', 'university')
