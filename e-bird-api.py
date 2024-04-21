import csv
import json
import pandas as pd
import requests as rq
from requests import JSONDecodeError

#EBIRD API
api_key = "2hig7s0jt391"
header = {"x-ebirdapitoken": api_key}
base_url = "https://api.ebird.org/v2"

vinderhoute_durmeers = "L13909784"
vinderhoute_durmeers_lat = 51.0871423
vinderhoute_durmeers_long = 3.6546237


vinderhoutse_bossen = "L11300818"
vinderhoutse_bossen_lat = 51.0776865
vinderhoutse_bossen_long = 3.65155

bourgoyen_ossemeersen_id = "L13536525"
bourgoyen_ossemmeersen_lat = 51.0551747
bourgoyen_ossemmeersen_long = 3.6764048

apple_orchard_beiaard_id = "L30676179"
apple_orchard_beiaard_lat = 51.09968
apple_orchard_beiaard_long = 3.63135

stewart_park_id = "L99381" #Stewart Park, Tompkins, New York, US location id
stewart_park_lat = 42.4613413
sterwart_park_long = -76.5054578
stewart_park_region_code = "US-NY-109" #country-subnational1-subnational2

#NUTHATCH API
def get_birds():
    url = 'https://nuthatch.lastelm.software/v2/birds'
    authorization = {'API-Key': '5bd7602b-514d-40bd-b705-d84c5f38ddc9'}
    params = {
        'pageSize': 100,
        #'pageNumber': 1,
        #'region': 'Western Europe'
        }
    response = connection_exception_caller(rq.get(url, params=params, headers=authorization))
    return response.json()

def show_birds_by_region(region, data):
    dictionary = list()
    birds = data.get('entities')
    for bird in birds:
        if region in bird['region']:
            dictionary.append(bird)
    return dictionary


def find_bird_by_name(name, data):
    dictionary = list()
    birds = data.get('entities')
    for bird in birds:
        if name in bird.get('name'):
            dictionary.append(bird)
    return dictionary

# local bird list -- natuurpunt --
local_bird_list = [
    'Common Woodpigeon',
    'Eurasian Blue Tit',
    'Coal Tit',
    'Dunnock',
    'Carrion Crow',
    'Common Chaffinch',
    'Long-tailed Tit',
    'Eurasian Wren',
    'House Sparrow',
    'Brambling',
    'Eurasian Jay',
    'Common Starling',
    'Eurasian Blackbird',
    'Song Thrush',
    'Eurasian Siskin',
    'Common Magpie',
    'European Robin',
    'Eurasian Jackdaw',
    'Eurasian Nuthatch',
    'Great Spotted Woodpecker'
]
# local bird scientific -- natuurpunt
local_bird_scientific_list = [
    'Sturnus vulgaris',
    'Corvus corone',
    'Garrulus glandarius',
    'Dendrocopos major',
    'Corvus monedula',
    'Periparus ater',
    'Cyanistes caeruleu',
    'Aegithalos caudatus',
    'Sitta europaea',
    'Troglodytes troglodytes',
    'Turdus philomelos',
    'Erithacus rubecula',
    'Prunella modularis',
    'Passer domesticus',
    'Fringilla coelebs',
    'Fringilla montifringilla',
    'Spinus spinus',
    'Columba palumbus',
    'Turdus merula',
    'Pica pica',
    'Streptopelia decaocto'
]

# get all recent observations by region code
def recent_observations_by_region(region_code):
    response = connection_exception_caller(rq.get(f'{base_url}/data/obs/{region_code}/recent', headers=header))
    return response.json()


#recent notable observations
def recent_notable_observations(region_code):
    response = connection_exception_caller(rq.get(f'{base_url}/data/obs/{region_code}/recent/notable', headers=header))
    return response.json()


#recent observations by species
def recent_observations_by_species(region_code, species_code):
    response = connection_exception_caller(rq.get(f'{base_url}/data/obs/{region_code}/recent/{species_code}', headers=header))
    return response.json()


#recent nearby observations by latitude / longitude
def recent_nearby_observations(latitude, longitude):
    response = connection_exception_caller(rq.get(f'{base_url}/data/obs/geo/recent?lat={latitude}&lng={longitude}', headers=header))
    return response.json()


#recent nearby observations by latitude / longitude and species code
def recent_nearby_observations_by_species(latitude, longitude, species_code):
    response = connection_exception_caller(rq.get(f'{base_url}/data/obs/geo/recent/{species_code}?lat={latitude}&lng={longitude}', headers=header))
    return response.json()


#nearest observation of species by latitude / longitude and species code
def nearest_observation_of_species(latitude, longitude, species_code):
    response = connection_exception_caller(rq.get(f'{base_url}/data/nearest/geo/recent/{species_code}?lat={latitude}&lng={longitude}', headers=header))
    return response.json()

#nearby notable observations by latitude / longitude

def nearby_notable_observations(latitude, longitude):
    response = connection_exception_caller(rq.get(f'{base_url}/data/obs/geo/recent/notable?lat={latitude}&lng={longitude}'))
    return response.json()
#recent checklists entered

def recent_checklists_feed(region_code):
    response = connection_exception_caller(rq.get(f'{base_url}/product/lists/{region_code}'))
    return response.json()

#historic observations by data
# region code - year, month, day
def historic_observations_on_date(region_code, year, month, day):
    response = connection_exception_caller(rq.get(f'{base_url}/data/obs/{region_code}/historic/{year}/{month}/{month}/{day}', headers=header))
    return response.json()

#The Top 100 contributors in region on a given date.
def top_100_contributors_by_region_and_date(region_code, year, month, day):
    response = connection_exception_caller(rq.get(f'{base_url}/product/top100/{region_code}/{year}/{month}/{day}', headers=header))
    return response.json()

#Checklists submitted in a region on a given date.
def checklist_feed_on_date_by_region(region_code, year, month, day):
    response = connection_exception_caller(rq.get(f'{base_url}/product/lists/{region_code}/{year}/{month}/{day}', headers=header))
    return response.json()

def regional_statistics_on_date(region_code, year, month, day):
    response = connection_exception_caller(rq.get(f'{base_url}/product/stats/{region_code}/{year}/{month}/{day}', headers=header))
    return response.json()

#Species codes occurring in a region
def species_code_list_of_region(region_code):
    response = connection_exception_caller(rq.get(f'{base_url}/product/spplist/{region_code}', headers=header))
    return response.json()


#View single checklist by id
def view_checklist_by_id(checklist_id):
    response = connection_exception_caller(rq.get(f'{base_url}/product/checklist/view/{checklist_id}', headers=header))
    return response.json()


#Find regions adjacent to region by regioncode
def find_adjacent_regions(region_code):
    response = connection_exception_caller(rq.get(f'{base_url}/ref/adjacent/{region_code}', headers=header))
    return response.json()


# find hotspots in region by regioncode
def find_hotspots_in_region(region_code):
    response = connection_exception_caller(rq.get(f'{base_url}/ref/hotspot/{region_code}', headers=header))
    return response.json()


# find nearby hotspots by latitude and longitude -!BUG - JSONDecode error-
# ! DEBUG ! -> fix jsonDecode error
def find_nearby_hotspots(latitude, longitude):
    response = connection_exception_caller(rq.get(f'{base_url}/ref/hotspot/geo?lat={latitude}&lng={longitude}', headers=header))
    return response.json()



def hotspot_info(hotspot_id):
    response = connection_exception_caller(rq.get(f'{base_url}/ref/hotspot/info/{hotspot_id}', headers=header))
    return response.json()


#region info by regioncode (region code build up: "BE" -> Belgium, country; "BE-VLG" -> Vlaams Gewest, subnational1)
def region_info(region_code):
    response = connection_exception_caller(rq.get(f'{base_url}/ref/region/info/{region_code}', headers=header))
    return response.json()


#Find the subregions of a given region by region type and region code
#Options for the type are world > country > subnational1 > subnational2
def sub_region_list(region_code, region_type):
    response = connection_exception_caller(rq.get(f'{base_url}/ref/region/list/{region_type}/{region_code}', headers=header))
    return response.json()


#make dataframe from species code list
def make_dataframe_from_species_code_list(data, species_code_list):
    dataframe_src = pd.read_csv(data, delimiter=',', encoding='latin-1')
    df = dataframe_src[['SCIENTIFIC_NAME', 'COMMON_NAME', 'SPECIES_CODE', 'EXTINCT']]
    df.columns = ['Scientific name', 'English name', 'Species code', 'Extinct']
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('expand_frame_repr', False)
    return df[df['Species code'].isin(species_code_list)]


#make dataframe of local birds Vlaams Gewest (smallest region in Belgium, subnational1)
def make_species_code_dataframe_vlg(data):
    dataframe_src = pd.read_csv(data, delimiter=',', encoding="latin-1")
    df = dataframe_src[['SCIENTIFIC_NAME', 'COMMON_NAME', 'SPECIES_CODE', 'EXTINCT']]
    df.columns = ['Scientific name', 'English name', 'Species code', 'Extinct']
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('expand_frame_repr', False)
    return df[df['Species code'].isin(species_code_list_of_region("BE-VLG"))]


#make dataframe based on scientific name;
def make_scientific_dataframe_from_csv(data, filter_array):
    dataframe_src = pd.read_csv(data, delimiter=',', encoding="latin-1")
    df = dataframe_src[['SCIENTIFIC_NAME', 'COMMON_NAME', 'SPECIES_CODE', 'EXTINCT']]
    df.columns = ['Scientific name', 'English name', 'Species code', 'Extinct']
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('expand_frame_repr', False)
    return df[df['Scientific name'].isin(filter_array)]


#pretty json
def pretty_json_builder(data):
    return json.dumps(data, indent=4, sort_keys=True)


#make dataframe from json
def make_dataframe_from_json(data):
    rows = list()
    for row in data:
        rows.append(row)

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    return pd.DataFrame(rows)


#make dataframe from dict list !BUG None type exception
# ! DEBUG ! -> Handle type None
def make_dataframe_from_list_of_dict(data):
    info = data.get('results')
    rows = []
    for sub in info:
        row = {'subId': sub.get('subId'), 'locId': sub.get('locId'), 'comments': sub.get('comments'),
               'checkListId': sub.get('checkListId'), 'subnational1Code': sub.get('subnational1Code'),
               'obs': sub.get('obs')}
        rows.append(row)

    return pd.DataFrame(rows)

#make csv from json
def make_csv_from_json(data):
    csv_file = 'output.csv'
    csv_obj = open(csv_file, 'w')
    csv_writer = csv.writer(csv_obj)
    columns = data[0].keys()
    csv_writer.writerow(columns)

    for item in data:
        csv_writer.writerow(item.values())
    csv_obj.close()

#make cs from dataframe
def make_csv_from_dataframe(data):
    dataframe = pd.DataFrame(data)
    csv_file = 'output.csv'
    dataframe.to_csv(csv_file, index=False)
#Exceptions
def connection_exception_caller(request):
    try:
        return request
    except ConnectionError:
        print("Connection to API failed.")
    except JSONDecodeError as e:
        print(e.strerror)

#print(pretty_json_builder(region_info("BE")))
#print(pretty_json_builder(region_info(apple_orchard_beiaard_id)))
#print(species_code_list_of_region(apple_orchard_beiaard_id))
#print(pretty_json_builder(view_checklist_by_id("S168902821")))
#print(pretty_json_builder(view_checklist_by_id("S169427154"))) #sparrowhawk spotting
#print(make_scientific_dataframe_from_csv('data/ebird-taxonomy.csv', local_bird_scientific_list))
#print(make_dataframe_from_species_code_list('data/ebird-taxonomy.csv', species_code_list_of_region(bourgoyen_ossemeersen_id))) #region = bourgoyen
#print(make_dataframe_from_species_code_list('data/ebird-taxonomy.csv', species_code_list_of_region(apple_orchard_beiaard_id))) #region = apple orchard beiaard


#print(region_info("BE"))
#print(hotspot_info())
#print(make_dataframe(get_birds()))
#print(pretty_json_builder(recent_observations_by_region("BE")))
#print(make_dataframe_from_list_of_dict(view_checklist_by_id("S169398828")))
#print(find_nearby_hotspots(apple_orchard_beiaard_lat, apple_orchard_beiaard_long))


#NUTHATCH API
#print(pretty_json_builder(get_birds()))
#print(pretty_json_builder(find_bird_by_name('Coal Tit', get_birds())))
