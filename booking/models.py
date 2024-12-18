from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    time = models.TimeField()
    total_seats = models.PositiveIntegerField()
    booked_seats = models.PositiveIntegerField(default=0)

    @property
    def seat_status(self):
        return "Fully Booked" if self.booked_seats >= self.total_seats else "Seats Available"

    def __str__(self):
        return f"{self.movie.title} - {self.time}"
