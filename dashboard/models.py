# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date, datetime


# Create your models here.
class Tables(models.Model):
    id = models.AutoField(primary_key=True)
    case_type = models.CharField(max_length=80)
    people_total_tested_count = models.IntegerField(null=True, default=0)
    cases = models.IntegerField(null=True, blank=True, default=0)
    difference = models.IntegerField(null=True, blank=True, default=0)
    date = models.DateField(auto_now_add=False, auto_now=False)
    combined_key = models.CharField(max_length=150)
    country_region = models.CharField(max_length=150)
    province_state = models.CharField(max_length=150)
    admin2 = models.TextField(blank=True, null=True)
    iso2 = models.CharField(max_length=80)
    iso3 = models.CharField(max_length=80)
    fips = models.IntegerField(null=True,default=0)
    lat = models.FloatField(null=True, blank=True, default=0)
    lon = models.FloatField(null=True, blank=True, default=0)
    population_count = models.IntegerField(null=True, blank=True)
    people_hospitalized = models.IntegerField(null=True, default=0)
    data_source = models.CharField(max_length=90)
    prep_flow_runtime = models.DateTimeField(auto_now_add=False, auto_now=False)
    objects = models.Manager()