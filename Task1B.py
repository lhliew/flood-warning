# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 16:13:48 2017

@author: laide
"""
"""prints a list of tuples (station name, town, distance) for the 10 closest
and the 10 furthest stations from the Cambridge city centre, (52.2053, 0.1218)."""

from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    #Input coordinates of Cambridge city centre
    Reference_coordinate = (52.2053, 0.1218)

    #Create list of tuples (station name, distance)
    TheList = stations_by_distance (build_station_list(), Reference_coordinate)
    
    #Create list of tuples (station name, town, distance) for the 10 closest and furthest stations
    closest = [(s.name, s.town, d) for s, d in TheList[:10]]
    furthest = [(s.name, s.town, d) for s, d in TheList[-10:]]
            
    print ("The closest 10 stations are:")
    print (closest)

    print ("The furthest 10 stations are:")
    print (furthest)

if __name__ == "__main__":
    run()