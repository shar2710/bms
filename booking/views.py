from django.shortcuts import render
from .models import Showtime

def showtimes(request):
    showtimes = Showtime.objects.all()
    for showtime in showtimes:
        showtime.status = showtime.seat_status

    return render(request, 'booking/showtimes.html', {'showtimes': showtimes})
