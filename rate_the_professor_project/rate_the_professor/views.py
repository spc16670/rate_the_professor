# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from rate_the_professor.models import Rating, Professor


def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # RECENT RATINGS
    recent_ratings = Rating.objects.order_by('-id')[:12]

    # TOP 5
    top_professors = Professor.objects.order_by('-overall_rating')[:5]

     # BOTTOM 5
    bottom_professors = Professor.objects.order_by('overall_rating')[:5]
    context_dict = {'recent_ratings': recent_ratings, 'top_professors': top_professors,
                    'bottom_professors': top_professors}

    # Render the response and send it back!
    return render_to_response('rate_the_professor/index.html', context_dict, context)