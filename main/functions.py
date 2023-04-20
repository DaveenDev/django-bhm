import requests
import json
from inventory.models import InvLocation

def get_provinces():
    try:
        req = requests.get('https://psgc.gitlab.io/api/provinces/')
        provinces = json.loads(req.text)
        #from the result, convert it into a tuple of tuples which choicefield accepts
        sorted_list =  sorted(list(provinces),key=lambda k: k['name'], reverse=False)
        provinces_list = tuple([(p['code'],p['name']) for p in sorted_list])  
    except:
        provinces_list = []
    #print(provinces_list)
    return provinces_list

def get_regionx12_cities():
    try:
        req = requests.get('https://psgc.gitlab.io/api/regions/120000000/cities-municipalities/')
        data = json.loads(req.text)
        cities = [(city['code'],city['name']) for city in data]
    except:
        cities = []
    #print(cities)
    return cities

def get_categories():
    # create an empty entry to allow empty selection     
    request_api = requests.get('http://127.0.0.1:8000/api/categories/')
    category_list = json.loads(request_api.text)
    category_list = [{'id': cat['id'], 'name': cat['name']} for cat in category_list['results']]
    category_list.insert(0, {'id': 0, 'name': ''})
    return category_list

def get_units():
    # create an empty entry to allow empty selection     
    request_api = requests.get('http://127.0.0.1:8000/api/units/')
    units_list = json.loads(request_api.text)
    units_list = [{'id': unit['id'], 'unit': unit['unit']} for unit in units_list['results']]    
    return units_list

def get_locations():
    location = InvLocation.objects.all().values('id','name')
    return location

def get_default_location_id():
    id = InvLocation.objects.filter(name='Default')[0]
    return id

def debug_esc(code):
    return f'\033[{code}m'