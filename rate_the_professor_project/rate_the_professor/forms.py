from django import forms
from rate_the_professor.models import Rating, Professor, UserProfile, Course, Suggestion
from django.contrib.auth.models import User


# Used along with UserProfileForm to register a new user
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


# Used along with UserForm to register a new user
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('university', 'picture')


# Used to obtain a rating
class RatingForm(forms.ModelForm):
    communication = forms.DecimalField(initial=0, help_text="Communication ")
    knowledge = forms.DecimalField(initial=0, help_text="Knowledge ")
    approachability = forms.DecimalField(initial=0, help_text="Approachability ")
    enthusiasm = forms.DecimalField(initial=0, help_text="Enthusiasm ")
    clarity = forms.DecimalField(initial=0, help_text="Clarity ")
    awesomeness = forms.DecimalField(max_digits=2, decimal_places=1, initial=0, help_text="Awesomeness ")
    comment = forms.CharField(widget=forms.Textarea, max_length=1024, help_text="Comment ")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Rating
        fields = ('communication', 'knowledge', 'approachability', 'enthusiasm', 'clarity', 'awesomeness', 'comment')


# Used by users who wish to suggest a professor
#class ProfessorForm(forms.ModelForm):
#    title = forms.CharField(max_length=64, help_text="Title")
#    first_name = forms.CharField(max_length=256, help_text="First Name")
#    last_name = forms.CharField(max_length=256, help_text="Last Name")
#    website_url = forms.URLField(max_length=200, help_text="Website URL")

#    class Meta:
#        # Provide an association between the ModelForm and a model
#        model = Professor
#        fields = ('title', 'first_name', 'last_name', 'website_url', 'university', 'picture', 'university')


# Used by users who wish to suggest a professor
class SuggestionForm(forms.ModelForm):
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Suggestion
        fields = ('title', 'first_name','last_name', 'university','courses_taught')