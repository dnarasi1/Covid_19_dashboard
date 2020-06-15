# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
import imports as imp


from models import Tables
import logic as log
import json


# Create your views here.
lati = []
longi = []
ids = []
country_set = []
case_set = []
country_death = []
case_death = []
state_set = []
st_case_set = []
st_death = []
st_case_death = []
pop_country = []
pop_per = []
dateso = []
caseso = []
dateso1 = []
caseso1 = []


def imports(request):
    imp.get_data("C:\\Users\\Hello\\Documents\\dheeraj\\covid_dashboard\\dashboard\\COVID-19_cases.csv")
    return render_to_response('test.html')


def graphs(request):
    return render_to_response('graphs.html', {'country_set': json.dumps(country_set, default=str), 'case_set':
                                                    json.dumps(case_set, default=str),
                                                    'country_death': json.dumps(country_death, default=str),
                                                    'case_death':
                                                    json.dumps(case_death, default=str)})


def state_graphs(request):
    return render_to_response('state_graph.html', {'state_case': json.dumps(state_set, default=str),
                                                    'st_case':
                                                        json.dumps(st_case_set, default=str),
                                                    'state_death': json.dumps(st_death, default=str),
                                                    'st_case_death':
                                                        json.dumps(st_case_death, default=str)})


def complete_list(request):
    temp1 = zip(country_set, case_set)
    temp2 = zip(country_death, case_death)
    temp3 = zip(state_set, st_case_set)
    temp4 = zip(st_death, st_case_death)
    temp5 = zip(pop_country, pop_per)

    return render_to_response('complete.html', {'country_set': temp1, 'country_death': temp2, 'state_set': temp3,
                                                    'state_death': temp4, 'perc': temp5})


def checking(request):
    geo_json = [{
                "type": "Feature",
                 "properties": {
                     "id": ident,
                 },
                 "geometry": {
                     "type": "Point",
                     "coordinates": [lon, lat]}}
                for ident, lon, lat in zip(ids, longi, lati)]

    return render_to_response('map.html', {'geo_json': json.dumps(geo_json)})


def test(request):
    data = Tables.objects.all()
    count_conf, count_death, state_conf, state_death, totals, dates_sort, \
    location_sort, location_us_sort, population_sort = log.start_counting(data)

    for i in range(len(dates_sort)):
        dateso.append(dates_sort[i][0])
        caseso.append(dates_sort[i][1])

    x =0
    for i in range(len(dates_sort)):
        x = x+dates_sort[i][1]
        dateso1.append(dates_sort[i][0])
        caseso1.append(x)

    for i in range(len(location_sort)):
        lati.append(location_sort[i][0][0])
        longi.append(location_sort[i][0][1])
        ids.append(location_sort[i][1])

    geo_json = [{
                "type": "Feature",
                 "properties": {
                     "id": ident,
                 },
                 "geometry": {
                     "type": "Point",
                     "coordinates": [lon, lat]}}
                for ident, lon, lat in zip(ids, longi, lati)]

    world_total = 4286703
    world_deaths = 293467
    us_total = 1421055
    us_death = 85043

    for i in range(len(count_conf)):
        country_set.append(count_conf[i][0])
        case_set.append(count_conf[i][1])

    for i in range(len(count_death)):
        country_death.append(count_death[i][0])
        case_death.append(count_death[i][1])

    for i in range(len(state_conf)):
        state_set.append(state_conf[i][0])
        st_case_set.append(state_conf[i][1])

    for i in range(len(state_death)):
        st_death.append(state_death[i][0])
        st_case_death.append(state_death[i][1])

    for i in range(len(population_sort)):
        pop_country.append(population_sort[i][0])
        pop_per.append(population_sort[i][1])

    return render_to_response('dash_chartjs.html', {'world_c': world_total,
                                                    'world_d': world_deaths, 'us_c': us_total, 'us_d': us_death,
                                                    'geo_json': geo_json, 'dateso': json.dumps(dateso, default=str),
                                                    'caseso': json.dumps(caseso, default=str),
                                                    'dateso1': json.dumps(dateso1, default=str),
                                                    'caseso1': json.dumps(caseso1, default=str)
                                                    })
