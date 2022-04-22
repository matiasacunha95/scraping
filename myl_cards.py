''' Script that obtains all myl PB cards by edition '''

import json
import requests
from constants import editions, \
                      base_api_url

def export_data_to_file(filename, data):
    #Write given data to json file with 4 spaces indentation and utf-8 codification
    with open(f'{filename}.json', 'w') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)

def get_configs(edition):
    #Get data from request and build a json object
    data = requests.get(base_api_url + edition)
    data = json.loads(data.content)
    export_data_to_file('races', data['races'])
    export_data_to_file('rarities', data['rarities'])
    export_data_to_file('types', data['types'])
    export_data_to_file('keywords', data['keywords'])

def get_data(edition):
    #Get data from request and build a json object
    data = requests.get(base_api_url + edition)
    data = json.loads(data.content)
    export_data_to_file(edition + '-cards', data['cards'])
    export_data_to_file(edition, data['edition'])

def main():
    editions_data = []
    get_configs('undefined') 

    for edition in editions:
        get_data(edition)
   
if __name__ == '__main__':
    main()
