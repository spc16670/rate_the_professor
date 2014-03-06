# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from rate_the_professor.models import Rating, Professor, UserProfile
from rate_the_professor.forms import UserForm, UserProfileForm, RatingForm


def index(request):

    context = RequestContext(request)
    # RECENT RATINGS
    recent_ratings = Rating.objects.order_by('-id')[:12]
    # TOP 5
    top_professors = Professor.objects.order_by('-overall_rating')[:5]
     # BOTTOM 5
    bottom_professors = Professor.objects.order_by('overall_rating')[:5]
    context_dict = {'recent_ratings': recent_ratings, 'top_professors': top_professors,
                    'bottom_professors': bottom_professors}
    return render_to_response('rate_the_professor/index.html', context_dict, context)


def professor(request, professor_id):
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = RatingForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # an object that hasnt yet been saved to the database
            rating = form.save(commit=False)
            rating.user = request.user
            rating.professor = Professor(id=professor_id)
            # save!
            form.save()

            professor = Professor.objects.get(id=professor_id)
            sum_of_ratings = professor.sum_of_ratings
            no_of_ratings = professor.no_of_ratings
            new_ratings = no_of_ratings + 1
            Professor.objects.filter(pk=professor_id).update(no_of_ratings=new_ratings)
            new_sum = sum_of_ratings + rating.rating
            Professor.objects.filter(pk=professor_id).update(sum_of_ratings=new_sum)
            new_overall = new_sum / new_ratings
            Professor.objects.filter(pk=professor_id).update(overall_rating=new_overall)
        else:
            pass
    else:
        form = RatingForm()

    context_dict = {'professor_id': professor_id}
    try:
        professor = Professor.objects.get(id=professor_id)
        ratings = Rating.objects.filter(professor=professor_id)
        context_dict['ratings'] = ratings
        context_dict['professor'] = professor
    except Professor.DoesNotExist:
        pass
    context_dict['form'] = form
    return render_to_response('rate_the_professor/professor.html', context_dict, context)


def register(request):
    context = RequestContext(request)
    registered = False
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user
            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            # Now we save the UserProfile model instance.
            profile.save()
            # Update our variable to tell the template registration was successful.
            registered = True
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    # Render the template depending on the context.
    return render_to_response('rate_the_professor/register.html', {'user_form': user_form, 'profile_form': profile_form,
                                                                   'registered': registered}, context)


def user_login(request):
    context = RequestContext(request)
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/rate_the_professor/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rate the Professor account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("<font color='whist'>Invalid login details supplied.</font>")
    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('rate_the_professor/login.html', {}, context)


 # Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/rate_the_professor/')