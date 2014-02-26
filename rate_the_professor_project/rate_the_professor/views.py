# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from rate_the_professor.models import Rating, Professor


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
    context_dict = {'professor_id': professor_id}
    try:
        professor = Professor.objects.get(id=professor_id)
        ratings = Rating.objects.filter(fk_professor=professor_id)
        context_dict['ratings'] = ratings
        context_dict['professor'] = professor
    except Professor.DoesNotExist:
        pass
    return render_to_response('rate_the_professor/professor.html', context_dict, context)