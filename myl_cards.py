''' Script that obtains all myl cards by edition '''

import json
import requests
from constants import editions, \
                      base_api_url

def export_data_to_file(filename, data):
    #Write given data to json file with 4 spaces indentation and utf-8 codification
    with open(f'{filename}.json', 'w') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)

def get_data(edition):
    #get data from request and build a json object
    data = requests.get(base_api_url + edition)
    data = json.loads(data.content)
    print(data)
    export_data_to_file(edition, data)

def main():
    editions_data = []
    for edition in editions:
        get_data(edition)
   
if __name__ == '__main__':
    main()
