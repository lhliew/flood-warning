"""Unit test for the geo module"""

import pytest
from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, stations_by_rivers,rivers_by_station_number
from floodsystem.station import MonitoringStation


"""This tests the function stations_by_distance by making sure the distance 
and name of the station is outputed correctly in the right order in the tuple 
and with the right values."""
def test_stations_by_distance():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    #Build an empty list for storing tuples later
    Example_build_list = []
    Example_build_list.append(s)
    
    #calling the function to be tested
    Example_list = stations_by_distance(Example_build_list, (2.0, -4.0))
    
    #testing the values of the 2 elements in the tuple in the list
    for s, d in Example_list[:]:
        assert s.name == "some station"
        assert d == 994.3960016965921
        
def test_stations_within_radius():
    
    # Create 2 stations        
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    s_id = "test-s-id2"
    m_id = "test-m-id2"
    label = "A station"
    coord = (2.0, -4.05)
    trange = (-2.3, 3.4445)
    river = "River Y"
    town = "My Town B"
    t = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    #Build an empty list for storing tuples later
    Example_build_list = []
    Example_build_list.append(s)
    Example_build_list.append(t)
    
    #calling the function to be tested
    Example_list = stations_within_radius(Example_build_list, (2.0, -4.0), 10)
    Alphabetic_Example_List = sorted(Example_list)
    #tests that the list only shows statioins within radius
    assert Alphabetic_Example_List[0] == "A station"
    
    #calling the function to be tested
    Example_list = stations_within_radius(Example_build_list, (2.0, -4.0), 1000)
    Alphabetic_Example_List = sorted(Example_list)
    #tests that the list sorts it alphabetically
    assert Alphabetic_Example_List[0] == "A station"
    assert Alphabetic_Example_List[1] == "some station"

def test_rivers_with_station():
     # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    
    s_id = "test-s-id2"
    m_id = "test-m-id2"
    label = "A station"
    coord = (2.0, -4.05)
    trange = (-2.3, 3.4445)
    river = "River Y"
    town = "My Town B"
    t = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    #Build an empty list for storing tuples later
    Example_build_list = []
    Example_build_list.append(s)
    Example_build_list.append(t)
    
    k = rivers_with_station(Example_build_list)
    
    assert len(k) == 2

def test_stations_by_rivers():
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    
    s_id = "test-s-id2"
    m_id = "test-m-id2"
    label = "A station"
    coord = (2.0, -4.05)
    trange = (-2.3, 3.4445)
    river = "River Y"
    town = "My Town B"
    t = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    #Build an empty list for storing tuples later
    Example_build_list = []
    Example_build_list.append(s)
    Example_build_list.append(t)
    
    testdict = stations_by_rivers(Example_build_list)
    
    a = testdict["River X"]

    assert a == ["some station"]

def test_rivers_by_station_number():
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "Station 1"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    
    s_id = "test-s-id2"
    m_id = "test-m-id2"
    label = "Station 2"
    coord = (2.0, -4.05)
    trange = (-2.3, 3.4445)
    river = "River Y"
    town = "My Town B"
    t = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    s_id = "test-s-id3"
    m_id = "test-m-id3"
    label = "Station 3"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    u = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
    #Build an empty list for storing tuples later
    Example_build_list = []
    Example_build_list.append(s)
    Example_build_list.append(t)
    Example_build_list.append(u)
    
    a = rivers_by_station_number(Example_build_list, 1)
    
    assert a == [('River X', 2)]
    

    


    
    
    