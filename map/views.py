from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Search
from .forms import SearchForm
import folium
from folium import plugins
import geocoder

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SearchForm()
    # address = Search.objects.all().last()
    addresses = Search.objects.all()
    # location = geocoder.osm(address)
    # lat = location.lat
    # lng = location.lng
    # country = location.country
    # if lat == None or lng == None:
    #     address.save()
    #     return HttpResponse('You address input is invalid')

    # Create Map Object
    m = folium.Map(location=[1.37, 32.29], zoom_start=6)

    # folium.Marker([lat, lng], tooltip='Click for more',
    #               popup=country).add_to(m)
    for i in addresses:
        location = geocoder.osm(i.address)  # Geocode address
        lat = location.lat
        lng = location.lng
        country = location.country

        if lat and lng:# Check for valid coordinates before adding marker
            folium.Marker([lat, lng], tooltip='Click for more',popup=i.address, icon=folium.Icon(color='orange')).add_to(m)
        else:
            pass
    # Get HTML Representation of Map Object
    m.fit_bounds(m.get_bounds())
    m = m._repr_html_()
    context = {
        'm': m,
        'form': form,
    }
    return render(request, 'index.html', context)

from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
import geocoder
import geopy.distance
from django.utils import timezone

def calculate_distance(coord1, coord2):
    return geopy.distance.distance(coord1, coord2).km

def map_page(request):
    # Retrieve the next closest event from the database
    today = timezone.now().date()
    future_events = Event.objects.filter(date__gte=today)
    if future_events.exists():
        next_closest_event = future_events.order_by('date').first()
        address = next_closest_event.address  # Assuming 'address' is the field for the event's address
    else:
        return HttpResponse('No future events found.')

    # Use geocoder to get the coordinates of the event's address
    location = geocoder.osm(address)
    event_lat = location.latlng[0] if location.latlng else None
    event_lng = location.latlng[1] if location.latlng else None

    # Check if the coordinates are valid
    if event_lat is None or event_lng is None:
        return HttpResponse('The event address could not be located.')

    # Attempt to get the user's current location
    user_location = geocoder.ip('me')
    user_latlng = user_location.latlng if user_location.ok else None

    # Set default location to Kampala if user's location is not available
    user_lat = user_latlng[0] if user_latlng else 0.3511  # Latitude for Kampala
    user_lng = user_latlng[1] if user_latlng else 32.5643  # Longitude for Kampala

    # Calculate the distance between the user and the event
    distance = calculate_distance((user_lat, user_lng), (event_lat, event_lng))

    # Prepare the context for the template
    context = {
        'event_lat': event_lat,
        'event_lng': event_lng,
        'user_lat': user_lat,
        'user_lng': user_lng,
        'distance': distance,
    }

    return render(request, 'map.html', context)
