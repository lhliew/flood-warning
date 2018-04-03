import pytest
import datetime
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
import matplotlib
from floodsystem.stationdata import build_station_list, update_water_levels

def test_polyfit():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    station_and_relative_water_levels = []
    
    for station in stations: 
        station_and_relative_water_levels.append((station.relative_water_level(), station.name, station))
    
    p = 2
    
    dt = 2
    dates, levels = fetch_measure_levels(stations[3].measure_id,
                                         dt=datetime.timedelta(days=dt))
    #fit data to a polynomial    
    x = matplotlib.dates.date2num(dates)
    y = levels
    
    #shift axis
    d0 = x-x[0]

    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(d0, y, p)
    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)
    
    assert len(poly(d0))==len(d0)