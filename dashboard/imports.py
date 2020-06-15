import csv
import models as mod
import datetime


def get_data(csv_file):
    dfile = open(csv_file, 'rb')
    reader = csv.reader(dfile)
    rownum = 0
    for row in reader:
        if rownum == 0:
            rownum += 1
        else:
            the_row = mod.Tables(case_type=row[0], people_total_tested_count=row[1], cases=row[2], difference=row[3],
                                 date=datetime.datetime.strptime(row[4], '%Y-%m-%d').date(), combined_key=row[5],
                                 country_region=row[6], province_state=row[7],
                                 admin2=row[8], iso2=row[9], iso3=row[10], fips=row[11], lat=row[12], lon=row[13],
                                 population_count=row[14], people_hospitalized=row[15], data_source=row[16],
                                 prep_flow_runtime=row[17])
            the_row.save()