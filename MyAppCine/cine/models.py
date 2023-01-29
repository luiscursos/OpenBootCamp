from django.db import models
import uuid

# Create your models here.
class Genre(models.Model):
    # Indicamos locampos que tendra en la bbdd
    film_genre = models.CharField(max_length=32, help_text="Enter the genre")

    def __str__(self):
        return self.film_genre

class Movie(models.Model):
    title = models.CharField(max_length=16,help_text="Enter the film's name")

    director = models.ForeignKey('Film_director', on_delete=models.SET_NULL, null=True)

    synopsis = models.TextField(max_length=100, help_text="Enter the film's summary")
    
    film_year = models.DateField(null=True, blank=True)
    
    # con on_delete=models.SET_NULL se mantiene la integridad referencial
    # Aqui indicamos que la película puede tener varios géneros asociados
    genre = models.ManyToManyField(Genre)


    def __str__(self):
        return self.title

class WhereSeeMovie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este libro")
    movie = models.ForeignKey('Movie', on_delete=models.SET_NULL, null=True)
    placeToSeeMovie=(
        ('c', 'Cine'),
        ('t', 'Tv'),
        ('v', 'VOD'),
    )
    status = models.CharField(max_length=1, choices=placeToSeeMovie, blank=True, default='c', help_text=("Donde ver la película"))
    
    
    def __str__(self):
        return '%s (%s)' %(self.id, self.movie.title)



class Film_director(models.Model):
    director_name = models.TextField(max_length=32)
    date_of_birth = models.DateField(null=True, blank=True)
    films = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.director_name




