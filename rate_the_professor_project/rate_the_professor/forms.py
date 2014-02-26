from django import forms
from rate_the_professor.models import Rating, Professor


class RatingForm(forms.ModelForm):
    communication = forms.DecimalField(initial=2.5)
    knowledge = forms.DecimalField(initial=2.5)
    approachability = forms.DecimalField(initial=2.5)
    enthusiasm = forms.DecimalField(initial=2.5)
    clarity = forms.DecimalField(initial=2.5)
    awesomeness = forms.DecimalField(initial=2.5)

    fk_user = forms.IntegerField(widget=forms.HiddenInput())
    fk_professor = forms.IntegerField(widget=forms.HiddenInput())

    comment = forms.CharField(max_length=1024, help_text="Please enter the comment here.")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Rating
        fields = ('communication', 'knowledge', 'approachability', 'enthusiasm', 'clarity', 'awesomeness', 'comment')


class ProfessorForm(forms.ModelForm):
    title = forms.CharField(max_length=64, help_text="Title")
    first_name = forms.CharField(max_length=256, help_text="First Name")
    last_name = forms.CharField(max_length=256, help_text="Last Name")

    #fk_university = models.ForeignKey(University)
    #fk_courses_taught = models.ManyToManyField(Course)

    #picture = https://docs.djangoproject.com/en/dev/ref/forms/api/#binding-uploaded-files
    website_url = forms.URLField(max_length=200, help_text="Website URL")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Professor

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        fields = ('title', 'first_name', 'last_name', '', '', 'website_url')
