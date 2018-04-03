"""Builds a list of all stations with inconsistent typical range data. 
    Print a list of stations names, in alphabetical order, 
    for stations with inconsistent data."""

from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    ListOfInconsistentStations = inconsistent_typical_range_stations(stations)

    print (sorted(ListOfInconsistentStations))

if __name__ == "__main__":
    run()