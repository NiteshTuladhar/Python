from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Movie, MovieLinks
from django.views.generic.dates import YearArchiveView



class MovieHome(ListView):
    model = Movie
    template_name= 'movie/home.html'

    def get_context_data(self, **kwargs):
        context = super(MovieHome, self).get_context_data(*kwargs)
        context['top_rated'] = Movie.objects.filter(status='TR')
        context['most_watched'] = Movie.objects.filter(status="MW")
        context['recently_added'] = Movie.objects.filter(status="RA")
        return context




class MovieList(ListView):
    model = Movie
    paginate_by = 5


class MovieDetail(DetailView):
    model = Movie


    def get_object(self):
        object = super(MovieDetail, self).get_object()
        object.veiws_count += 1
        object.save()
        return (object)

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['links'] = MovieLinks.objects.filter(movie=self.get_object())
        context['related_movies'] = Movie.objects.filter(category= self.get_object().category)
        return context



class MovieCategory(ListView):
    model = Movie
    paginate_by = 5

    def get_queryset(self):
        self.category = self.kwargs['category']
        movies = Movie.objects.filter(category=self.category)
        return movies



    def get_context_data(self,**kwargs):
        context = super(MovieCategory, self).get_context_data(*kwargs)
        context['movie_category'] = self.category
        return context

class MovieLanguage(ListView):
    model = Movie
    paginate_by = 5

    def get_queryset(self):
        self.language = self.kwargs['lang']
        movies = Movie.objects.filter(language=self.language)
        return movies



    def get_context_data(self,**kwargs):
        context = super(MovieLanguage, self).get_context_data(*kwargs)
        context['movies_language'] = self.language
        return context



class MovieSearch(ListView):
    model = Movie
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)

        else:
            object_list = self.model.none()

        return object_list

class MovieYear(YearArchiveView):
    queryset = Movie.objects.all()
    date_field = 'year_of_production'
    make_object_list = True
    allow_future = True

class MovieStatus(ListView):
    model = Movie
    paginate_by = 5

    def get_queryset(self):
        self.status = self.kwargs['status']
        movies = Movie.objects.filter(status=self.status)
        return movies



    def get_context_data(self,**kwargs):
        context = super(MovieStatus, self).get_context_data(*kwargs)
        context['movie_status'] = self.status
        return context