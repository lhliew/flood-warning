"""Unit test for the station module"""

import pytest
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town
    #testing if outputis true if typical range is consistent
    assert MonitoringStation.typical_range_consistent(s) == True

    #create inconsistent typical range for testing
    trange = (3.4445, -2.3)
    t = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert MonitoringStation.typical_range_consistent(t) == False

    #Create NoneType data to test
    trange = None
    u = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert MonitoringStation.typical_range_consistent(u) == False

""" Test the function inconsistent_typical_range_stations"""
def test_inconsistent_typical_range_stations():
    
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    Example_list =[]
    Example_list.append(s)
    Test_List = inconsistent_typical_range_stations(Example_list)
    assert Test_List == []

    #create inconsistent typical range for testing
    trange = (3.4445, -2.3)
    t = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    Example_list =[]
    Example_list.append(t)
    Test_List = inconsistent_typical_range_stations(Example_list)
    assert Test_List == ["some station"]

    #Create NoneType data to test
    trange = None
    u = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    Example_list =[]
    Example_list.append(u)
    Test_List = inconsistent_typical_range_stations(Example_list)
    assert Test_List == ["some station"]
