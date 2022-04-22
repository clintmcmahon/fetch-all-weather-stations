# encoding: utf-8

import sys
import datetime
import json
import requests


def get_stations(state):
    response = requests.post('https://data.rcc-acis.org/StnMeta', data={
                             "elems": "maxt,mint", "sdate": "1871-01-01", "edate": "2021-12-31", "state": state})
    data = response.json()
    return data["meta"]


def main():
    '''
    Main method
    '''
    stations = []
    states = open('states.json')
    statesData = json.load(states)
    for state in statesData:
        stations.append(
            {"name": state["name"], 
            "shortCode": state["shortCode"],
            "stations": get_stations(state["shortCode"])})

    with open('json_data.json', 'w') as outfile:
        json.dump(stations, outfile)


if __name__ == '__main__':
    main()
