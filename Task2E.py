""" plots the water levels over the past 10 days for the 5 stations at which 
the current relative water level is greatest"""

import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels

def run():
    
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    station_and_relative_water_levels = []
    
    for station in stations:
        station_and_relative_water_levels.append((station.relative_water_level(), station.name, station))

    stations_with_values_for_water_levels = []
    for x in station_and_relative_water_levels:  
        if x[0] is None:
            pass
        else:
            stations_with_values_for_water_levels.append(x)
            
    stations_with_values_for_water_levels.sort(reverse = True)
    
    """for n in stations_with_values_for_water_levels:
        dt = 10
        dates, levels = fetch_measure_levels(n[2].measure_id,
                                         dt=datetime.timedelta(days=dt))
        print(dates[0], dates [-1])
        print(dates[0]-dates[-1])
        if dates[0]-dates[-1] != dt-1:
            #cut n from list"""
    
    """find a way to automate removal stations with outdated data
    """
    
    greatest_5 = stations_with_values_for_water_levels[1:6]
    
    #Fetch data over past 10 days
    for n in greatest_5:
        dt = 10
        dates, levels = fetch_measure_levels(n[2].measure_id,
                                         dt=datetime.timedelta(days=dt))
        print(dates[0], dates [-1])
        #plot graph
        plot_water_levels (n[2], dates, levels)
    
    
if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")

    run()