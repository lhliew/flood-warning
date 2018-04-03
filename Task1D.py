# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 10:19:57 2017

@author: user 1
"""

from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_rivers
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    
    """ Part 1 of Task 1D
    """
    
    a = rivers_with_station(stations)
    
    """ Sorting the list of rivers
    """
    
    b = sorted(a)
    print (len(a), '\n')
    
    """Getting the first 10 entries
    """
    
    print (b[:10], '\n')
    
    
    """ Part 2 of Task 1D
    """
    riverdict = stations_by_rivers(stations)
    
    c= riverdict["River Aire"]
    d= riverdict["River Cam"]
    e= riverdict["Thames"]
    
    print (sorted(c), '\n' )
    print (sorted(d), '\n')
    print (sorted(e))


if __name__ == "__main__":
    print ("** Task 1D: CUED Part IA Flood Warning System **")
    run()