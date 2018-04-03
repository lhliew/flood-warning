# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 12:44:45 2017

@author: user 1
"""

import pytest
from floodsystem.flood import stations_level_over_threshold,stations_highest_rel_level
from floodsystem.station import MonitoringStation

def test_stations_level_over_threshold():
    
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

    a = stations_level_over_threshold (Example_build_list, 0.5)
    
    assert a == [] 
    
    
def test_stations_highest_rel_level():
    
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

    a = stations_highest_rel_level(Example_build_list, 5)
    
    assert a == [] 