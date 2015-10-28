# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 14:07:36 2015

@author: dutchman
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *


#import packages
from math import sqrt


def isoMeasurement(iso, p_x, p_y, hsize, vsize):
        # Measures for Isovist Arrays
        Area = 0
        Perimeter = 0
        mean_radial_length = 0
        gravity_center_x = 0
        gravity_center_y = 0
        radials = []
        
        # compute Measurements
        for y in range(1,vsize-1):
            for x in range(1,hsize-1):
                # Check if Pixel belongs to Isovist
                if (iso.pixel(x,y) == 0):
                    continue
                Area += 1
                # Check if Pixel belongs to Boundary
                if (iso.pixel(x-1,y) == 0 or iso.pixel(x+1,y) == 0 or iso.pixel(x,y-1) == 0 or iso.pixel(x,y+1) == 0):
                    Perimeter += 1
                    dist = (y-p_y)**2 + (x-p_x)**2;
                    dist = sqrt(dist);
                    mean_radial_length += dist
                    radials.append(dist)
                    gravity_center_x += x
                    gravity_center_y += y
                    
        # standart deviation
        mean_radial = float(mean_radial_length/Perimeter)
        std_dev = 0
        min_rad = 9999999
        max_rad = -1

        gravity_center_x /= Perimeter
        gravity_center_y /= Perimeter;

        drift = (gravity_center_x - p_x) * (gravity_center_x - p_x);
        drift += (gravity_center_y - p_y) * (gravity_center_y - p_y);
        drift = sqrt(drift);
        
        for it in radials:
            std_dev += (it-mean_radial) * (it-mean_radial)
            if (it > max_rad):
                max_rad = it
            if (it < min_rad):
                min_rad = it
        std_dev /= Perimeter
        std_dev = sqrt(std_dev)

        return Area,Perimeter,float(Area/Perimeter),drift,mean_radial,std_dev,max_rad,min_rad