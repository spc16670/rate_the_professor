# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from rate_the_professor.models import Rating, Professor, UserProfile, Course, User
from rate_the_professor.forms import UserForm, UserProfileForm, RatingForm, SuggestionForm
from decimal import Decimal


def index(request):
    context = RequestContext(request)
    # RECENT RATINGS
    recent_ratings = Rating.objects.order_by('-id')[:12]
    # TOP 5
    top_professors = Professor.objects.order_by('-overall_rating')[:5]
    # BEST COMMUNICATORS
    best_communicators = Professor.objects.order_by('-overall_communication')[:5]
     # EASILY APPROACHABLE
    easily_approachable = Professor.objects.order_by('-overall_approachability')[:5]

    context_dict = {'recent_ratings': recent_ratings
        , 'top_professors': top_professors
        , 'best_communicators': best_communicators
        , 'easily_approachable': easily_approachable
    }
    return render_to_response('rate_the_professor/index.html', context_dict, context)


def user(request):
    context = RequestContext(request)
    user_id = request.user.id
    context_dict = {'user_id': user_id}
    try:
        user = User.objects.get(id=user_id)
        context_dict['user'] = user
        #user_profile = User.user_profile

        context_dict['user_profile'] = UserProfile.objects.get(user=user)
        ratings = Rating.objects.filter(user=user_id)
        context_dict['ratings'] = ratings
    except User.DoesNotExist:
        pass
    return render_to_response('rate_the_professor/user.html', context_dict, context)


def professor(request, professor_id):
    context = RequestContext(request)
    context_dict = {'professor_id': professor_id}
    # A HTTP POST?
    if request.method == 'POST':
        form = RatingForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():

            # Save Rating object
            rating = form.save(commit=False)
            rating.user = request.user
            rating.professor = Professor(id=professor_id)
            # save!
            form.save()

            # Update Professor object
            professor = Professor.objects.get(id=professor_id)
            update_professor_scores(professor, rating)

            #Professor.objects.filter(pk=professor_id).update(overall_rating=new_overall)
            form = RatingForm()
        else:
            pass
    else:
        form = RatingForm()
    try:
        professor = Professor.objects.get(id=professor_id)
        ratings = Rating.objects.filter(professor=professor_id)
        context_dict['ratings'] = ratings
        context_dict['professor'] = professor
        courses_taught = Course.objects.filter(professor__id=professor_id)
        context_dict['courses_taught'] = courses_taught
    except Professor.DoesNotExist:
        pass
    context_dict['form'] = form
    return render_to_response('rate_the_professor/professor.html', context_dict, context)


def update_professor_scores(professor, rating):
    #communication
    no_of_communication = professor.no_of_communication + 1
    sum_of_communication = professor.sum_of_communication + rating.communication
    overall_communication = sum_of_communication / no_of_communication

    #knowledge
    no_of_knowledge = professor.no_of_knowledge + 1
    sum_of_knowledge = professor.sum_of_knowledge + rating.knowledge
    overall_knowledge = sum_of_knowledge / no_of_knowledge

    #approachability
    no_of_approachability = professor.no_of_approachability + 1
    sum_of_approachability = professor.sum_of_approachability + rating.approachability
    overall_approachability = sum_of_approachability / no_of_approachability

    #enthusiasm
    no_of_enthusiasm = professor.no_of_enthusiasm + 1
    sum_of_enthusiasm = professor.sum_of_enthusiasm + rating.enthusiasm
    overall_enthusiasm = sum_of_enthusiasm / no_of_enthusiasm

    #clarity
    no_of_clarity = professor.no_of_clarity + 1
    sum_of_clarity = professor.sum_of_clarity + rating.clarity
    overall_clarity = sum_of_clarity / no_of_clarity

    #awesomeness
    no_of_awesomeness = professor.no_of_awesomeness + 1
    sum_of_awesomeness = professor.sum_of_awesomeness + rating.awesomeness
    overall_awesomeness = sum_of_awesomeness / no_of_awesomeness

    #overall
    no_of_ratings = professor.no_of_ratings + 1
    sum_of_ratings = professor.sum_of_ratings + Decimal(rating.rating)
    overall_rating = sum_of_ratings / no_of_ratings

    professor_id = professor.id
    Professor.objects.filter(pk=professor_id).update(

        no_of_communication=no_of_communication
        , sum_of_communication=sum_of_communication
        , overall_communication=overall_communication

        , no_of_knowledge=no_of_knowledge
        , sum_of_knowledge=sum_of_knowledge
        , overall_knowledge=overall_knowledge

        , no_of_approachability=no_of_approachability
        , sum_of_approachability=sum_of_approachability
        , overall_approachability=overall_approachability

        , no_of_enthusiasm=no_of_enthusiasm
        , sum_of_enthusiasm=sum_of_enthusiasm
        , overall_enthusiasm=overall_enthusiasm

        , no_of_clarity=no_of_clarity
        , sum_of_clarity=sum_of_clarity
        , overall_clarity=overall_clarity

        , no_of_awesomeness=no_of_awesomeness
        , sum_of_awesomeness=sum_of_awesomeness
        , overall_awesomeness=overall_awesomeness

        , no_of_ratings=no_of_ratings
        , sum_of_ratings=sum_of_ratings
        , overall_rating=overall_rating
    )

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
    return render_to_response('rate_the_professor/register.html', {
        'user_form': user_form
        , 'profile_form': profile_form
        , 'registered': registered}, context)


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
                # js will send the user back to the homepage.
                login(request, user)
                return HttpResponse('/')
                #return HttpResponseRedirect('/rate_the_professor/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rate the Professor account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            #return HttpResponse("<font color='whist'>Invalid login details supplied.</font>")
            return HttpResponseForbidden()
    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('rate_the_professor/login.html', {}, context)


    #defines a view which will handle the suggest a professor form
def suggestion (request):
    context = RequestContext(request)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        suggestion_form = SuggestionForm(data=request.POST)
        # If the form is valid
        if suggestion_form.is_valid():
            # Save the suggestion form data to the database.
            suggestion_form.save(commit=True)

            return index(request)
        else:
            print suggestion_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        suggestion_form = SuggestionForm()
    # Render the template depending on the context.
    return render_to_response('rate_the_professor/suggestion.html', {'suggestion_form':suggestion_form
        }, context)



def get_professors_list(max_results=0, starts_with=''):
        prof_list = []
        if starts_with:
            prof_list = Professor.objects.filter(last_name__istartswith=starts_with)
        else:
            prof_list = Professor.objects.all()
        if max_results > 0:
            if len(prof_list) > max_results:
                prof_list = prof_list[:max_results]

        return prof_list


def suggest_professor(request):
        context = RequestContext(request)
        prof_list = []
        starts_with = ''
        if request.method == 'GET':
                starts_with = request.GET['suggestion']
                max_results = int(request.GET['max_results'])
        prof_list = get_professors_list(max_results, starts_with)
        return render_to_response('rate_the_professor/professor_suggestions.html', {'prof_list': prof_list}, context)

 # Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/rate_the_professor/')