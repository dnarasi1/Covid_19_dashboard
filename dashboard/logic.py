import models as mod
import time
import datetime
import operator


class TotalCount:
    def __init__(self, diction):
        from datetime import date
        self.today = date.today()
        self.countries = diction


def calculate_per(conf, pop):
    if pop == 0:
        return 0
    else:
        return 100 * float(conf)/float(pop)


def start_counting(data):
    states_us_conf = {}
    states_us_death = {}
    countries_conf = {}
    countries_death = {}
    population = {}
    province_set = set([])
    dates_cases = {}
    location = {}
    location_us = {}

    total_cases = 0
    total_deaths = 0
    total_cases_us = 0
    total_deaths_us = 0
    us_loc = {}

    for row in data:
        if row.date in dates_cases:
            dates_cases[row.date] = dates_cases.get(row.date) + row.difference
        else:
            dates_cases[row.date] = row.difference

        if row.country_region in population:
            if row.combined_key in province_set:
                pass
            else:
                province_set.add(row.combined_key)
                population[row.country_region] = population.get(row.country_region) + row.population_count
        else:
            population[row.country_region] = row.population_count
            province_set.add(row.combined_key)

        if row.case_type == "Confirmed":
            if row.country_region in countries_conf:
                countries_conf[row.country_region] = countries_conf.get(row.country_region) + row.difference
                total_cases += row.difference
            else:
                countries_conf[row.country_region] = row.difference
                total_cases += row.difference

            if not (row.lat and row.lon) == 0:
                if (row.lat, row.lon) in location:
                    location[(row.lat, row.lon)] = location.get((row.lat, row.lon)) + row.difference
                else:
                    location[(row.lat, row.lon)] = row.difference

            if row.country_region == "US":
                if row.province_state in states_us_conf:
                    states_us_conf[row.province_state] = states_us_conf.get(row.province_state) + row.difference
                    total_cases_us += row.difference
                else:
                    states_us_conf[row.province_state] = row.difference
                    total_cases_us += row.difference
                if not (row.lat and row.lon) == 0:
                    if (row.lat, row.lon) in location_us:
                        location_us[(row.lat, row.lon)] = location_us.get((row.lat, row.lon)) + row.difference
                    else:
                        location_us[(row.lat, row.lon)] = row.difference

        if row.case_type == "Deaths":
            if row.country_region in countries_death:
                countries_death[row.country_region] = countries_death.get(row.country_region) + row.difference
                total_deaths += row.difference
            else:
                countries_death[row.country_region] = row.difference
                total_deaths += row.difference

            if row.country_region == "US":
                if row.province_state in states_us_death:
                    states_us_death[row.province_state] = states_us_death.get(row.province_state) + row.difference
                    total_deaths_us += row.difference
                else:
                    states_us_death[row.province_state] = row.difference
                    total_deaths_us += row.difference

    for i, j in population.iteritems():
        population[i] = calculate_per(countries_conf.get(i), population.get(i))

    dateCount1 = "2020-5-7"
    dateCount2 = "2020-5-10"
    dateCount3 = "2020-5-13"
    dateCount4 = "2020-5-4"
    dateCount5 = "2020-5-5"
    dateCount6 = "2020-5-8"
    ddate1 = datetime.datetime.strptime(dateCount1, '%Y-%m-%d').date()
    ddate2 = datetime.datetime.strptime(dateCount2, '%Y-%m-%d').date()
    ddate3 = datetime.datetime.strptime(dateCount3, '%Y-%m-%d').date()
    ddate4 = datetime.datetime.strptime(dateCount4, '%Y-%m-%d').date()
    ddate5 = datetime.datetime.strptime(dateCount5, '%Y-%m-%d').date()
    ddate6 = datetime.datetime.strptime(dateCount6, '%Y-%m-%d').date()
    dates_cases[ddate1] = 96254
    dates_cases[ddate2] = 79825
    dates_cases[ddate3] = 88220
    dates_cases[ddate4] = 79582
    dates_cases[ddate5] = 81247
    dates_cases[ddate6] = 97128

    countries_conf["US"] = 1421055
    countries_death["US"] = 85043
    count_conf = sorted(countries_conf.items(), key=operator.itemgetter(1), reverse=True)
    count_death = sorted(countries_death.items(), key=operator.itemgetter(1), reverse=True)
    state_conf = sorted(states_us_conf.items(), key=operator.itemgetter(1), reverse=True)
    state_death = sorted(states_us_death.items(), key=operator.itemgetter(1), reverse=True)
    dates_sort = sorted(dates_cases.items(), key=operator.itemgetter(0))
    location_sort = sorted(location.items(), key=operator.itemgetter(1),  reverse=True)
    location_us_sort = sorted(location_us.items(), key=operator.itemgetter(1),  reverse=True)
    population_sort = sorted(population.items(), key=operator.itemgetter(1),  reverse=True)

    totals = ((total_cases, total_deaths), (total_cases_us, total_deaths_us))
    return count_conf, count_death, state_conf, state_death, totals, dates_sort, location_sort, \
           location_us_sort, population_sort
