# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 01:00:40 2017

@author: user 1
"""
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    stations = build_station_list()
    
    update_water_levels(stations) 
    
    first_N_stations = stations_highest_rel_level(stations, 10)
    
    for i in range(len(first_N_stations)):
        print(first_N_stations[i][0].name, first_N_stations[i][1])
    
    
    
if __name__ == "__main__":
    print ("** Task 2C: CUED Part IA Flood Warning System **")
    run()