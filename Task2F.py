"""plots the water level data and the best-fit polynomial"""

import datetime
import matplotlib.pyplot as plt
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit

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
    greatest_5 = stations_with_values_for_water_levels[1:6]
    
    p = 4
    for n in greatest_5:
        #Fetch data over past 2 days
        dt = 2
        dates, levels = fetch_measure_levels(n[2].measure_id,
                                         dt=datetime.timedelta(days=dt))
        #fit data to a polynomial
        k = polyfit(dates, levels, p)
        #plot graph with data and also polynomial
        plot_water_level_with_fit(n[2], dates, levels, k)
        #plot lines of typical high and low
        plt.axhline(n[2].typical_range[0], linewidth=2, color='r')
        plt.axhline(n[2].typical_range[1], linewidth=2, color='r')
        plt.show()
    

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    

    run()
