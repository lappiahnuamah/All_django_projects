from django.shortcuts import render
from .models import City
from django.views.generic import TemplateView, ListView
from django.db.models import Q

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = City
    template_name = 'search_results.html'
     
    # def get_queryset(self): # new
    #     return City.objects.filter(name__icontains='Boston')
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list =  City.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        print(type(object_list))
        return object_list

