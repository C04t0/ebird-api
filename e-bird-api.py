import json
import pandas as pd
import requests as rq

api_key = "2hig7s0jt391"
header = {"x-ebirdapitoken": api_key}
base_url = "https://api.ebird.org/v2"


def recent_observations_by_region(region_code):
    response = rq.get(f'{base_url}/data/obs/{region_code}/recent', headers=header)
    return response.json()

def recent_notable_observations(region_code):
    response = rq.get(f'{base_url}/data/obs/{region_code}/recent/notable', headers=header)
    return response.json()

def recent_observations_by_species(region_code, species_code):
    response = rq.get(f'{base_url}/data/obs/{region_code}/recent/{species_code}', headers=header)
    return response.json()

def recent_nearby_observations(latitude, longitude):
    response = rq.get(f'{base_url}/data/obs/geo/recent?lat={latitude}&lng={longitude}', headers=header)
    return response.json()

def recent_nearby_observations_by_species(latitude, longitude, species_code):
    response = rq.get(f'{base_url}/data/obs/geo/recent/{species_code}?lat={latitude}&lng={longitude}', headers=header)
    return response.json()

def nearest_observation_of_species(latitude, longitude, species_code):
    response = rq.get(f'{base_url}/data/nearest/geo/recent/{species_code}?lat={latitude}&lng={longitude}', headers=header)
    return response.json()

def nearby_notable_observations(latitude, longitude):
    response = rq.get(f'{base_url}/data/obs/geo/recent/notable?lat={latitude}&lng={longitude}')
    return response.json()

def recent_checklists_feed(region_code):
    response = rq.get(f'{base_url}/product/lists/{region_code}')
    return response.json()

def historic_observations_on_date(region_code, year, month, day):
    response = rq.get(f'{base_url}/data/obs/{region_code}/historic/{year}/{month}/{month}/{day}', headers=header)
    return response.json()

#The Top 100 contributors in region on a given date.
def top_100_contributors_by_region_and_date(region_code, year, month, day):
    response = rq.get(f'{base_url}/product/top100/{region_code}/{year}/{month}/{day}', headers=header)
    return response.json()

#Checklists submitted in a region on a given date.
def checklist_feed_on_date_by_region(region_code, year, month, day):
    response = rq.get(f'{base_url}/product/lists/{region_code}/{year}/{month}/{day}', headers=header)
    return response.json()

def regional_statistics_on_date(region_code, year, month, day):
    response = rq.get(f'{base_url}/product/stats/{region_code}/{year}/{month}/{day}', headers=header)
    return response.json()

#Species codes occurring in a region
def species_code_list_of_region(region_code):
    response = rq.get(f'{base_url}/product/spplist/{region_code}', headers=header)
    return response.json()

def view_checklist_by_id(checklist_id):
    response = rq.get(f'{base_url}/product/checklist/view/{checklist_id}', headers=header)
    return response.json()

def find_adjacent_regions(region_code):
    response = rq.get(f'{base_url}/ref/adjacent/{region_code}', headers=header)
    return response.json()

def find_hotspots_in_region(region_code):
    response = rq.get(f'{base_url}/ref/hotspot/{region_code}', headers=header)
    return response.json()

def find_nearby_hotspots(latitude, longitude):
    response = rq.get(f'{base_url}/ref/hotspot/geo?lat={latitude}&lon={longitude}', headers=header)
    return response.json()

def hotspot_info(hotspot_id):
    response = rq.get(f'{base_url}/ref/hotspot/info/{hotspot_id}', headers=header)
    return response.json()

def region_info(region_code):
    response = rq.get(f'{base_url}/ref/region/info/{region_code}', headers=header)
    return response.json()

#Find the subregions of a given region by region type and region code
#Options for the type are country > subnational1 > subnational2
def sub_region_list(region_code, region_type):
    response = rq.get(f'{base_url}/ref/region/list/{region_type}/{region_code}', headers=header)
    return response.json()

def make_taxonomy_dataframe_from_csv(file):
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    return pd.read_csv(file, delimiter=',', encoding='latin-1')


#Helper functions
def pretty_json_builder(data):
    return json.dumps(data, indent=2)

def make_dataframe(data):
    rows = list()

    for row in data:
        rows.append(row)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)

    return pd.DataFrame(rows)

def connection_exception_caller(request):
    try:
        return request
    except ConnectionError:
        print("Connection to API failed.")


#print(pretty_json_builder(recent_observations_by_region("BE")))
#print(make_dataframe(recent_observations_by_region("BE")))

#print(pretty_json_builder(species_code_list_of_region("BE")))
#print(pretty_json_builder(connection_exception_caller(region_info("BE"))))
print(make_taxonomy_dataframe_from_csv('data/ebird-taxonomy.csv'))
