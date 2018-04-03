""" list the towns where the risk of flooding is assessed to be greatest. """

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

    """if got time, try using polynomial
    p = 4
    for n in stations_with_values_for_water_levels:
        #Fetch data over past 2 days
        dt = 2
        dates, levels = fetch_measure_levels(n[2].measure_id,
                                         dt=datetime.timedelta(days=dt))
        #fit data to a polynomial
        k = polyfit(dates, levels, p)
        #extrapolate the polynomial to see if it passes high or severe in 1 day"""
        
    Low_risk = []
    Moderate_risk = []
    High_risk = []
    Severe_risk = []
        
    for n in stations_with_values_for_water_levels:
        if n[0] < 0.25:
            Low_risk.append((n[0], n[1]))
        elif 0.25 <= n[0] < 0.9:
            Moderate_risk.append((n[0], n[1]))
        elif 0.9 <= n[0] < 1.5:
            High_risk.append((n[0], n[1]))
        elif n[0] >= 1.5:
            Severe_risk.append((n[0], n[1]))
            
    Low_risk.sort(reverse = True)
    Moderate_risk.sort(reverse = True)
    High_risk.sort(reverse = True)
    Severe_risk.sort(reverse = True)

    #print ("Low risk")
    #print (Low_risk[:5])
    #print ("Moderate risk")
    #print (Moderate_risk[:5])
    print ("High risk")
    print (High_risk[:5])
    print ("Severe risk")
    print (Severe_risk[:5])
            
if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    

    run()
