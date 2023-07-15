from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
import json, os, math
from math import radians, sin, cos, sqrt, atan2
from scipy.spatial.distance import pdist, squareform
from tsp_solver.greedy import solve_tsp
import tsp_solver
from .models import *
from django.core import serializers
from django.urls import reverse
from django.db.models import Count
from decimal import Decimal
from django.shortcuts import render
from django.db.models import Q
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from math import radians, cos, sin, sqrt, atan2
from itertools import permutations
from scipy.spatial.distance import pdist, squareform
from tsp_solver.greedy import solve_tsp


# The 'sklearn' module refers to scikit-learn, which is a popular
# machine learning library in Python that includes various clustering
#  algorithms, including DBSCAN.
from sklearn.cluster import DBSCAN
import numpy as np
import random

# Create your views here.
def accueil(request):
    circuitVoyage = CircuitVoyage.objects.all()
    # Get all Destination objects for Targets section 
    all_destinations = Destination.objects.all()
    # Get 7 random destinations
    random_destinations = random.sample(list(all_destinations), 5)
    # Get all Materiels objects for Targets section 
    all_Moussem =Moussem.objects.all()
    random_Moussem = random.sample(list(all_Moussem), 8)
    # Get all Ville objects for Targets section 
    all_Ville =Ville.objects.all()
    random_Ville = random.sample(list(all_Ville), 6)
    # Get all plat objects for Targets section 
    all_Plat =Plat.objects.all()
    random_Plat = random.sample(list(all_Plat), 6)

    context = {
        'circuitVoyage': circuitVoyage,
        'random_destinations': random_destinations,
        'random_Moussem' : random_Moussem,
        'random_Ville' : random_Ville,
        'random_Plat' : random_Plat,

            
        }
    return render(request, "accueil.html", context)


def test(request):
    destination = Destination.objects.all()
    return render(
        request,
        "test.html",
        {
            "destination": destination,
        },
    )


# creation d un fichier json pour a partire d un A QuerySet
# The Destination.objects.all() method returns a QuerySet object, not a list or dictionary
def genere_ciruit(request):
    selected_destinations = request.POST.getlist("destination")
    destinations = Destination.objects.filter(id_dest__in=selected_destinations)
    # destinations = Destination.objects.all()[0:5]
    # Create a list to store the serialized fields
    serialized_data = []
    # Serialize the fields for each model object
    for destination in destinations:
        serialized_fields = {
            "id_dest" : destination.id_dest,
            "nom_dest": destination.nom_dest,
            "ville_dest": destination.ville_dest,
            "province": destination.province,
            "image_dest1": destination.image_dest1,
            "image_dest2": destination.image_dest2,
            "image_dest3": destination.image_dest3,
            #'localisation_dest': destination.localisation_dest,
            #'carte_dest': destination.carte_dest,
            "description_dest": destination.description_dest,
            #'date_modification': destination.date_modification,
            "latitude": destination.latitude,
            "longitude": destination.longitude,
        }
        serialized_data.append(serialized_fields)
    # Convert the serialized data to JSON
    json_data = json.dumps(serialized_data, indent=4)

    # Specify the file path for the JSON file
    file_path = os.path.join(
        os.path.dirname(__file__), "static", "json", "circuit.json"
    )
    # Save the serialized data into the JSON file
    with open(file_path, "w") as file:
        file.write(json_data)
    url = reverse("myapp:circuit")
    return redirect(url)


""" def circuit(request):
    # creation des variable
    circuit_json_files = "items_draa_tafilalet.json"
    circuit_json_files1 = "circuit.json"

    # todo genere the absulte
    file_path = os.path.join(
        os.path.dirname(__file__), "static", "json", circuit_json_files1
    )
    with open(file_path, "r") as f:
        # create a new file for writing
        data = json.load(f)
        # write the list of cities to the new file using json.dump()
        # cities = data["cities"]
        cities = data
    # todo a list ville that work
    with open(file_path) as f:
        données = json.load(f)
        # ville = json.dumps(données["cities"])
        ville = json.dumps(données)
    # todo creation d un tuple qui contion list of tuple  (31.918953, -4.445651)
    city_tuples = []
    for city in cities:
        latitude = float(city["latitude"])
        longitude = float(city["longitude"])
        city_tuple = (latitude, longitude)
        city_tuples.append(city_tuple)
    # todo calculate the distance matrix
    distances = pdist(city_tuples, "euclidean")
    # todo Create distance matrix qui contion dist_matrix
    dist_matrix = squareform(distances)
    # todo solve TSP using tsp_solver library
    path = solve_tsp(dist_matrix)
    # todo reorder city tuples based on the TSP path
    ordered_cities = [city_tuples[i] for i in path]
    
    context = {
        "Destinations": cities,
        "ville": ville,
        "city_tuples": city_tuples,
        "ordered_cities": ordered_cities,
    }
    return render(request, "circuit_destination.html", context)
 """


def circuit(request):
    selected_circuit = request.GET.get("circuit")
    circuit_json_files = f"json{selected_circuit}.json"

    file_path = os.path.join(os.path.dirname(__file__), "static", "json", circuit_json_files)

    with open(file_path, "r") as f:
        cities = json.load(f)

    ville = json.dumps(cities)

    city_tuples = []
    for city in cities:
        latitude = float(city["latitude"])
        longitude = float(city["longitude"])
        categorie = city["categorie"]
        city_tuple = {
            "lat": latitude,
            "lng": longitude,
            "categorie": categorie
        }
        city_tuples.append(city_tuple)

    city_coordinates = np.array([(city["lat"], city["lng"]) for city in city_tuples])
    distances = np.linalg.norm(city_coordinates[:, None] - city_coordinates, axis=-1)
    dist_matrix = distances.astype(np.float64)

    path = solve_tsp(dist_matrix)
    ordered_cities = [city_tuples[i] for i in path]

    context = {
        "Destinations": cities,
        "ville": ville,
        "city_tuples": city_tuples,
        "ordered_cities": ordered_cities,
    }

    return render(request, "chosiCircuit.html", context)


def about(request):
    # all ville that exist on my Destination models
    villes = Destination.objects.values_list("ville_dest", flat=True).distinct()

    destinations_by_ville = {}
    for ville in villes:
        destinations = Destination.objects.filter(ville_dest=ville)
        destinations_by_ville[ville] = destinations

    # Now you have a dictionary where the keys are the ville names and the values are the corresponding destinations
    # You can pass this dictionary to your template context

    return render(
        request, "about.html", {"destinations_by_ville": destinations_by_ville}
    )


# fonction that help use create destination page dynamique
def destination_page(request, destination_id):
    # destination = get_object_or_404(Destination, id=destination_id)
    # Perform any required actions using the destination object
    destination = Destination.objects.get(id_dest=destination_id)
    google_maps_link = destination.localisation_dest
    #retire la ville de distination que l utilisateur cherch 
    ville_destination=destination.ville_dest 
    #retire tout les  Restaurant de distination que l utilisateur cherch 
    restaurants = Restaurant.objects.filter(ville_rest=ville_destination)
    #retire tout les hotel de distination que l utilisateur cherch 
    Hotels=Hotel.objects.filter(ville_hot=ville_destination)

    context = {
        "destination": destination, 
        "restaurants" :restaurants,
        'hotels' : Hotels,
        }
    return render(request, "destination_detail.html", context)

# fonction that help use create 40 html page dynamique
def hotel_page(request, hotel_id):
    # retire un hotel de id 
    hotel = Hotel.objects.get(id_hotel=hotel_id)


    context = {
        "hotel":hotel,
        }
    return render(request, "hotel_detail.html", context)

def restaurant_page(request, Restaurant_id):
    # retire un hotel de id 
    restaurant = Restaurant.objects.get(id_rest=Restaurant_id)


    context = {
        "restaurant":restaurant,
        }
    return render(request, "restaurant_detail.html", context)

def ville_page(request, id_ville):
    # retire un hotel de id 
    ville = Ville.objects.get(ville_id=id_ville)
    print(ville)

    context = {
        "ville":ville,
        }
    return render(request, "ville_detail.html", context)

# function that give use 7 destination


""" def genere_un_circuit(request):
    start_destination_name = request.GET.get('start_destination')
    end_destination_name = request.GET.get('end_destination')
    # Retrieve all destinations from the database
    destinations = Destination.objects.all()

    # Extract the latitude and longitude features from the destinations
    features = np.array([
        [destination.latitude, destination.longitude]
        for destination in destinations
    ])

    # Set the parameters for DBSCAN
    epsilon = 0.1  # The maximum distance between two samples to be considered in the same neighborhood
    min_samples = 5  # The minimum number of samples in a neighborhood to be considered a core point

    # Apply DBSCAN to the feature data
    dbscan = DBSCAN(eps=epsilon, min_samples=min_samples)
    clusters = dbscan.fit_predict(features)

    # Find the cluster with the largest number of points
    unique_clusters, cluster_counts = np.unique(clusters, return_counts=True)
    largest_cluster = unique_clusters[np.argmax(cluster_counts)]

    # Get the indices of destinations belonging to the largest cluster
    indices = np.where(clusters == largest_cluster)[0].astype(int)[:12]

    # Filter the destinations based on the indices
    largest_cluster_destinations = destinations.filter(id_dest__in=list(indices))

    # Pass the selected destinations to the template
    context = {
        'selected_destinations': largest_cluster_destinations
    }

    return render(request, 'genere_un_circuit.html', context) """


def genere_un_circuit(request):
    # Retrieve start and end destinations from the form
    start_destination_name = request.GET.get("arrival")
    end_destination_name = request.GET.get("departure")

    # Retrieve all destinations from the database
    destinations = Destination.objects.all()

    # Extract the latitude and longitude features from the destinations
    features = np.array(
        [[destination.latitude, destination.longitude] for destination in destinations]
    )

    # Set the parameters for DBSCAN
    epsilon = 0.1  # The maximum distance between two samples to be considered in the same neighborhood
    min_samples = 5  # The minimum number of samples in a neighborhood to be considered a core point

    # Apply DBSCAN to the feature data
    dbscan = DBSCAN(eps=epsilon, min_samples=min_samples)
    clusters = dbscan.fit_predict(features)

    # Find the cluster with the largest number of points
    unique_clusters, cluster_counts = np.unique(clusters, return_counts=True)
    largest_cluster = unique_clusters[np.argmax(cluster_counts)]

    # Get the indices of destinations belonging to the largest cluster
    indices = np.where(clusters == largest_cluster)[0].astype(int)[:12]

    # Filter the destinations based on the indices
    largest_cluster_destinations = destinations.filter(id_dest__in=list(indices))

    # Rearrange the destinations to place the start and end destinations at the beginning and end
    if start_destination_name and end_destination_name:
        # Retrieve the start and end destinations from the filtered destinations
        start_destination = largest_cluster_destinations.get(
            nom_dest=start_destination_name
        )
        end_destination = largest_cluster_destinations.get(
            nom_dest=end_destination_name
        )

        # Exclude the start and end destinations from the filtered destinations
        largest_cluster_destinations = largest_cluster_destinations.exclude(
            nom_dest=start_destination_name
        ).exclude(nom_dest=end_destination_name)

        # Create a new list to rearrange the destinations
        rearranged_destinations = (
            [start_destination] + list(largest_cluster_destinations) + [end_destination]
        )

        # Pass the rearranged destinations to the template
        context = {"selected_destinations": rearranged_destinations}
    else:
        # Pass the original filtered destinations to the template
        context = {"selected_destinations": largest_cluster_destinations}

    return render(request, "genere_un_circuit.html", context)




def contact(request):
    return render(request, "contact.html")


def services(request):
    return render(request, "services.html")




# version work 
""" def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in kilometers
    lat1_rad, lon1_rad, lat2_rad, lon2_rad = map(radians, [lat1, lon1, lat2, lon2])
    
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = sin(dlat / 2) ** 2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    distance = R * c
    return distance

def tsp(start_latitude, start_longitude, end_latitude, end_longitude, intermediate_cities):
    # Create the list of all cities, including the start and end points
    cities = [Ville(latitude=start_latitude, longitude=start_longitude)] + list(intermediate_cities) + [Ville(latitude=end_latitude, longitude=end_longitude)]
    
    # Generate all possible permutations of cities
    permutations_list = list(permutations(cities))

    shortest_distance = float('inf')
    shortest_path = []

    # Iterate through each permutation
    for permutation in permutations_list:
        total_distance = 0

        # Calculate the total distance of the current permutation
        for i in range(len(permutation) - 1):
            city1 = permutation[i]
            city2 = permutation[i + 1]
            total_distance += calculate_distance(city1.latitude, city1.longitude, city2.latitude, city2.longitude)

        # Check if the current permutation has a shorter distance
        if total_distance < shortest_distance:
            shortest_distance = total_distance
            shortest_path = permutation

    return shortest_path
 """

""" def search_cities(request):
    start_ville = request.GET.get('start_ville')
    end_ville = request.GET.get('end_ville')

    try:
        start_city = Ville.objects.get(ville_name=start_ville)
        end_city = Ville.objects.get(ville_name=end_ville)

        start_latitude = start_city.latitude
        start_longitude = start_city.longitude
        end_latitude = end_city.latitude
        end_longitude = end_city.longitude

        intermediate_cities = Ville.objects.filter(
            latitude__gte=min(start_latitude, end_latitude),
            latitude__lte=max(start_latitude, end_latitude),
            #longitude__gte=min(start_longitude, end_longitude),
            #longitude__lte=max(start_longitude, end_longitude)
        ).exclude(ville_name__in=[start_city.ville_name, end_city.ville_name])
        
        print(intermediate_cities)
        # Apply the TSP algorithm
        shortest_path = tsp(start_latitude, start_longitude, end_latitude, end_longitude, intermediate_cities)
        nbv = len(shortest_path) - 2  # Number of cities between start_city and end_city
        print('******************************************')
        print(nbv)
        # Convert the shortest_path into the format expected by the Leaflet map
        ordered_cities = [
            {'lat': city.latitude, 'lng': city.longitude, 'province': city.ville_name}
            for city in shortest_path[1:-1]  # Exclude the start and end cities from the loop
        ]
        ordered_cities.insert(0, {'lat': start_latitude, 'lng': start_longitude, 'province': start_city.ville_name})
        ordered_cities.append({'lat': end_latitude, 'lng': end_longitude, 'province': end_city.ville_name})
        # ordered_cities use for lefleat
        print(ordered_cities)
        villes = list(shortest_path[1:-1])  # Convert tuple to a list
        villes.insert(0, start_city)  # Add start_city at the beginning
        villes.append(end_city)
        context = {
            'start_city': start_city,
            'end_city': end_city,
            'cities': villes,
            'nbv': nbv,
            'ordered_cities': ordered_cities,
        }

        #return render(request, 'search_cities.html', context)
        return render(request, 'circuit_ville.html', context)
    except Ville.DoesNotExist:
        error_message = 'Start city or end city not found.'
        return render(request, 'error.html', {'error_message': error_message})
 """########## END version work


def tsp(start_latitude, start_longitude, end_latitude, end_longitude, intermediate_cities):
    # Create the list of all cities, including the start and end points
    cities = [
        (float(start_latitude), float(start_longitude), ""),
        *((float(city.latitude), float(city.longitude), city.ville_name) for city in intermediate_cities),
        (float(end_latitude), float(end_longitude), "")
    ]

    # Extract the coordinates for distance calculation
    coordinates = [(lat, lon) for lat, lon, _ in cities]

    # Calculate the pairwise distances between cities
    distances = pdist(coordinates, metric='euclidean')
    distance_matrix = squareform(distances)

    # Solve the TSP problem using the greedy solver from tsp_solver library
    shortest_path = solve_tsp(distance_matrix)

    # Convert the indices of cities to actual city coordinates
    ordered_cities = [cities[i] for i in shortest_path]

    return ordered_cities[1:-1] 

def search_cities(request):
    start_ville = request.GET.get('start_ville')
    end_ville = request.GET.get('end_ville')

    try:
        start_city = Ville.objects.get(ville_name=start_ville)
        end_city = Ville.objects.get(ville_name=end_ville)

        start_latitude = start_city.latitude
        start_longitude = start_city.longitude
        end_latitude = end_city.latitude
        end_longitude = end_city.longitude

        """ intermediate_cities = Ville.objects.filter(
            latitude__gte=min(start_latitude, end_latitude),
            latitude__lte=max(start_latitude, end_latitude),
            # longitude__gte=min(start_longitude, end_longitude),
            # longitude__lte=max(start_longitude, end_longitude)
        ).exclude(ville_name__in=[start_city.ville_name, end_city.ville_name]) """
        from django.db.models import Q
        
        """intermediate_cities = Ville.objects.filter(
            Q(latitude__gte=min(start_latitude, end_latitude), latitude__lte=max(start_latitude, end_latitude)) &
            Q(longitude__gte=min(start_longitude, end_longitude), longitude__lte=max(start_longitude, end_longitude))
        ).exclude(ville_name__in=[start_city.ville_name, end_city.ville_name]) """
        from django.db.models import Q

        extra_interval = Decimal('0.3')   # Specify the additional interval value here
        intermediate_cities = Ville.objects.filter(
            Q(latitude__gte=min(start_latitude, end_latitude) - extra_interval, latitude__lte=max(start_latitude, end_latitude) + extra_interval) &
            Q(longitude__gte=min(start_longitude, end_longitude) - extra_interval, longitude__lte=max(start_longitude, end_longitude) + extra_interval)
        ).exclude(ville_name__in=[start_city.ville_name, end_city.ville_name])


        print("fffffffffffffffffffffffffffffffffffffffff")
        print(intermediate_cities)
        # Apply the TSP algorithm
        ordered_cities = tsp(start_latitude, start_longitude, end_latitude, end_longitude, intermediate_cities)
        nbv = len(ordered_cities)  # Number of cities between start_city and end_city
        print("/////////////////////////////////////////////////")
        print(nbv)
        print("/////////////////////////////////////////////////")
        print(ordered_cities)
        # Convert the ordered_cities into the format expected by the Leaflet map
        # Convert the ordered_cities into the format expected by the Leaflet map
        ordered_cities = [{'lat': lat, 'lng': lon, 'province': prov} for lat, lon, prov in ordered_cities]
        ordered_cities.insert(0, {'lat': start_latitude, 'lng': start_longitude, 'province': start_city.ville_name})
        ordered_cities.append({'lat': end_latitude, 'lng': end_longitude, 'province': end_city.ville_name})
        
        villes = list(intermediate_cities)
        villes.insert(0, start_city)
        villes.append(end_city)

        context = {
            'start_city': start_city,
            'end_city': end_city,
            'cities': villes,
            'nbv': nbv,
            'ordered_cities': ordered_cities,
        }

        # return render(request, 'search_cities.html', context)
        return render(request, 'circuit_ville.html', context)
    except Ville.DoesNotExist:
        error_message = 'Start city or end city not found.'
        return render(request, 'error.html', {'error_message': error_message})


# version work ********
""" def tsp(cities, start_latitude, start_longitude, start_city):
    # Generate all possible permutations of the cities
    permutations_list = list(permutations(cities))

    # Initialize variables
    shortest_distance = float('inf')
    shortest_path = []

    # Iterate through each permutation
    for permutation in permutations_list:
        path = [start_city] + list(permutation) + [start_city]
        total_distance = 0

        # Calculate the total distance of the current permutation
        for i in range(len(path) - 1):
            city1 = path[i]
            city2 = path[i + 1]
            total_distance += calculate_distance(city1.latitude, city1.longitude, city2.latitude, city2.longitude)

        # Check if the current permutation has a shorter distance
        if total_distance < shortest_distance:
            shortest_distance = total_distance
            shortest_path = path

    return shortest_path
 """
""" def search_cities(request):
    start_ville = request.GET.get('start_ville')
    end_ville = request.GET.get('end_ville')

    try:
        start_city = Ville.objects.get(ville_name=start_ville)
        end_city = Ville.objects.get(ville_name=end_ville)

        start_latitude = start_city.latitude
        start_longitude = start_city.longitude
        end_latitude = end_city.latitude
        end_longitude = end_city.longitude

        cities = Ville.objects.filter(
            latitude__gte=min(start_latitude, end_latitude),
            latitude__lte=max(start_latitude, end_latitude),
            longitude__gte=min(start_longitude, end_longitude),
            longitude__lte=max(start_longitude, end_longitude)
        ).exclude(ville_name__in=[start_city.ville_name, end_city.ville_name])

        # Apply the TSP algorithm
        shortest_path = tsp(cities, start_latitude, start_longitude, start_city)

        nbv = len(shortest_path) - 2  # Number of cities between start_city and end_city

        context = {
            'start_city': start_city,
            'end_city': end_city,
            'cities': shortest_path[1:-1],
            'nbv': nbv,
        }

        return render(request, 'search_results.html', context)

    except Ville.DoesNotExist:
        error_message = 'Start city or end city not found.'
        return render(request, 'error.html', {'error_message': error_message})
 """
########## END version work ******


##### take a list of distination and use tsp and redirect to circuit_destination

def Tcircuit(request):
    selected_destinations = request.POST.getlist('destination')

    destinations = Destination.objects.filter(id_dest__in=selected_destinations)

    city_tuples = [(float(dest.latitude), float(dest.longitude), dest.categorie) for dest in destinations]

    city_coordinates = np.array([(float(dest.latitude), float(dest.longitude)) for dest in destinations])
    distances = np.linalg.norm(city_coordinates[:, None] - city_coordinates, axis=-1)
    dist_matrix = distances.astype(np.float64)

    path = solve_tsp(dist_matrix)

    # ordered_cities = [city_tuples[i] for i in path]
    #prepare lobjet pour lefleat 
    ordered_cities = [{'lat': city_tuples[i][0], 'lng': city_tuples[i][1], 'categorie': city_tuples[i][2]} for i in path]

    #end ajout 
    context = {
        'Destinations': destinations,
        'ordered_cities': ordered_cities,
    }
    return render(request, 'chosiCircuit.html', context)


""" def Tcircuit(request): """
"""     selected_destinations = request.POST.getlist('destination')

    destinations = Destination.objects.filter(id_dest__in=selected_destinations)

    city_tuples = [(float(dest.latitude), float(dest.longitude), dest.province) for dest in destinations]

    city_coordinates = np.array([(float(dest.latitude), float(dest.longitude)) for dest in destinations])
    distances = np.linalg.norm(city_coordinates[:, None] - city_coordinates, axis=-1)
    dist_matrix = distances.astype(np.float64)

    path = solve_tsp(dist_matrix)

    # ordered_cities = [city_tuples[i] for i in path]
    #prepare lobjet pour lefleat 
    ordered_cities = [{'lat': city_tuples[i][0], 'lng': city_tuples[i][1], 'province': city_tuples[i][2]} for i in path]

    #end ajout 
    context = {
        'Destinations': destinations,
        'ordered_cities': ordered_cities,
    }
    return render(request, 'circuit_destination.html', context) """