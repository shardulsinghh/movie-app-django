import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eco_energy_assignment.settings')
django.setup()

import json


from movieapp.models import Movie, Genre
from django.core.management.base import BaseCommand
from datetime import datetime

from django.core import serializers

from movieapp.api.serializers import MovieSerializer
 

def foo():
    with open('moviedata.json') as data_file:
        data = json.load(data_file)
    

    with open('db.json') as data_file:   #db.json has been generated from the provided input data
        genredata = json.load(data_file)
    genrekey = {}
    for genre in genredata:
        fields = genre["fields"]
        genrekey[fields["title"]] = genre["pk"]
        genreObj = Genre(title=fields["title"])
        genreObj.save()


    id = 1
    for movie in data:
        m = Movie( id = id, name = movie["name"], popularity= movie["99popularity"], director= movie["director"],imdb_score= movie["imdb_score"])
        for gen in movie["genre"]:
            genreObject = Genre.objects.get(title = gen.strip())
            m.save()
            genreObject.save()
            m.genre.add(genreObject)

        m.save()
        print('Saved: ', movie['name'])
        id+=1

foo() 
