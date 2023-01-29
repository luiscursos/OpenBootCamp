from django.shortcuts import render
from .models import Genre, Movie, Film_director, WhereSeeMovie

# Create your views here.

# Creamos la funcion index que recibe un parametro que es la petición(request)
def index(request):
    # Obtenemos los datos y los contamos en cada linea correspondiente
    num_movies = Movie.objects.all().count()
    num_geners = Genre.objects.all().count()
    num_directors = Film_director.objects.all().count()
    num_seeMovies = WhereSeeMovie.objects.all().count()

    ToSee = WhereSeeMovie.objects.filter(status__exact='t').all().count()


    return render(  # devolvemos un render con la request de arriba
        request,
        'index.html', # Indicamos que fichero html va a mostrar el contenido
        context={       # Esta plantilla va a tener unos datos que es este diccionario
             'num_movies': num_movies,
             'num_directors': num_directors,
             'ToSee': ToSee,
             'num_seeMovies': num_seeMovies,
             'num_geners': num_geners,
             
              
        }
    )