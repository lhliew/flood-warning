# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 17:31:50 2017

@author: user 1
"""
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    stations = build_station_list()
        
    update_water_levels(stations) 
    
    stations_over_threshold = stations_level_over_threshold(stations, 0.7)
    
    for i in range(len(stations_over_threshold)):
        print(stations_over_threshold[i][0].name, stations_over_threshold[i][1])

        
if __name__ == "__main__":
    print ("** Task 2B: CUED Part IA Flood Warning System **")
    run()