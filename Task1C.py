"""build a list of stations within 10 km of the Cambridge city centre (coordinate (52.2053, 0.1218))"""

from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    #x is the coordinate of the centre
    x = (52.2053, 0.1218)
    
    #runs function station_within_radius
    StationsNearCentre = stations_within_radius (build_station_list(), x, 10)

    #sorts the list alphabetically and prints it
    print(sorted(StationsNearCentre))


if __name__ == "__main__":
    run()