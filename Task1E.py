# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

""" Task 1E
"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

stations = build_station_list()

"""
Reuse the dictionary 

dictionary = stations_by_rivers(stations)
 
Count the len of the value of the dictionary

dictionary2 = {key: len(value) for key,value in dictionary.items()}

Sort the dictionary according to the value 
convert the dictionary into tuples

a = dictionary2.items()
print (a)

Print only the number that is required.


Oops discovered something better in python library. Used that instead. 

"""

"""
Changes made to geo.py
"""

def run():
    # Put code here that demonstrates functionality
    print (rivers_by_station_number(stations, 9))

if __name__ == "__main__":
    print ("** Task 1E: CUED Part IA Flood Warning System **")
    run()
