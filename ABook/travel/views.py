from django.shortcuts import render
from.models import Destination

# Create your views here.
def home(request):
#    return HttpResponse("<h1>hello world</h1?");

    dest1 = Destination()
    dest1.name = 'Nagrcoil'
    dest1.img = 'destination_1.jpg'
    dest1.address = 'Kanyakumari'
    dest1.desc = 'Srees 7 Nights 7 Star'
    dest1.price = 5000
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Palayankotai'
    dest2.address = 'Tirunelveli'
    dest2.img = 'destination_2.jpg'
    dest2.desc = 'Mani 4 Nights 4 Star'
    dest2.price = 4000
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Thiruvananthapuram'
    dest3.img = 'destination_3.jpg'
    dest3.address = 'Kerala'
    dest3.desc = 'Kandan 5 Nights 5 Star'
    dest3.price = 4500
    dest3.offer = False

    dests = (dest1,dest2,dest3)

    return render(request, 'home.html', {'dests': dests})