# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 14:26:48 2015

@author: dutchman
"""
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from math import sqrt

def computeIso(img, visible, visible2, p_x,p_y,size, illegal, hsize, vsize):
            # Artefact Filter
            for x in range(1,hsize-1):
                for y in range(1,vsize-1):
                    # check if illegal
                    art = 0
                    if (img.pixel(x,y) == illegal):
                        # check all neighbours
                        if (img.pixel(x+1,y) == illegal):
                            art += 1                             
                        if (img.pixel(x-1,y) == illegal):
                            art += 1
                        if (img.pixel(x,y+1) == illegal):
                            art += 1
                        if (img.pixel(x,y-1) == illegal):
                            art += 1
                        if (img.pixel(x+1,y+1) == illegal):
                            art += 1
                        if (img.pixel(x-1,y-1) == illegal):
                            art += 1 
                        if (img.pixel(x+1,y-1) == illegal):
                            art += 1
                        if (img.pixel(x-1,y+1) == illegal):
                            art += 1
                        # if artefact found - change color
                        if (art < 1):
                            img.setPixel(x,y,illegal+1)                        
            
            # compute isovist
            for i in range(size):
                # upper row
                y = p_y - i
                for x in range(p_x-i,p_x+i):
                    # check for boundarys
                    if (y < 0 or x < 0 or y > vsize or x > hsize):
                        continue
                    # compute distance
                    dist = (y-p_y)**2 +(x-p_x)**2
                    dist = sqrt(dist)
                    
                    # check if in circle
                    if (dist > size):
                        continue
                    
                    # Check for obstacle:
                    if (img.pixel(x,y) == illegal):
                        visible.setPixel(x,y,0)
                        continue
                        
                    # left half of upper row
                    if (x < p_x):
                        if (visible.pixel(x,y+1) == 0 or visible.pixel(x+1,y+1) == 0):
                            visible.setPixel(x,y,0)
                            continue
                    else:
                        if (visible.pixel(x,y+1) == 0 or visible.pixel(x-1,y+1) == 0):
                            visible.setPixel(x,y,0)
                            continue                    
                    # color point                    
                    img.setPixel(x,y,qRgb(qRed(img.pixel(x,y)),255,qBlue(img.pixel(x,y))))
                    #img.setPixel(x,y,qRgb(0,0,0))
                    visible2.setPixel(x,y,255)
                        
                        
                # lower row
                y = p_y + i
                for x in range(p_x-i,p_x+i):
                    # check for boundarys
                    if (y < 0 or x < 0 or y > vsize or x > hsize):
                        continue
                    # compute distance
                    dist = (y-p_y)**2 +(x-p_x)**2
                    dist = sqrt(dist)
                    
                    # check if in circle
                    if (dist > size):
                        continue
                    
                    # Check for obstacle:
                    if (img.pixel(x,y) == illegal):
                        visible.setPixel(x,y,0)
                        continue
                        
                    # left half of upper row
                    if (x < p_x):
                        if (visible.pixel(x,y-1) == 0 or visible.pixel(x+1,y-1) == 0):
                            visible.setPixel(x,y,0)
                            continue
                    else:
                        if (visible.pixel(x,y-1) == 0 or visible.pixel(x-1,y-1) == 0):
                            visible.setPixel(x,y,0)
                            continue                    
                    # color point
                    img.setPixel(x,y,qRgb(qRed(img.pixel(x,y)),255,qBlue(img.pixel(x,y))))
                    #img.setPixel(x,y,qRgb(0,0,0))
                    visible2.setPixel(x,y,255)                        
                    
                # left column
                x = p_x - i
                for y in range(p_y-i,p_y+i):
                    # check for boundarys
                    if (y < 0 or x < 0 or y > vsize or x > hsize):
                        continue
                    # compute distance
                    dist = (y-p_y)**2 +(x-p_x)**2
                    dist = sqrt(dist)
                    
                    # check if in circle
                    if (dist > size):
                        continue
                    
                    # Check for obstacle:
                    if (img.pixel(x,y) == illegal):
                        visible.setPixel(x,y,0)
                        continue
                        
                    # left half of upper row
                    if (y < p_y):
                        if (visible.pixel(x+1,y) == 0 or visible.pixel(x+1,y+1) == 0):
                            visible.setPixel(x,y,0)
                            continue
                    else:
                        if (visible.pixel(x+1,y) == 0 or visible.pixel(x+1,y-1) == 0):
                            visible.setPixel(x,y,0)
                            continue                    
                    # color point
                    img.setPixel(x,y,qRgb(qRed(img.pixel(x,y)),255,qBlue(img.pixel(x,y))))
                    #img.setPixel(x,y,qRgb(0,0,0))
                    visible2.setPixel(x,y,255)


                # right column
                x = p_x + i
                for y in range(p_y-i,p_y+i+1):
                    # check for boundarys
                    if (y < 0 or x < 0 or y > vsize or x > hsize):
                        continue
                    # compute distance
                    dist = (y-p_y)**2 +(x-p_x)**2
                    dist = sqrt(dist)
                    
                    # check if in circle
                    if (dist > size):
                        continue
                    
                    # Check for obstacle:
                    if (img.pixel(x,y) == illegal):
                        visible.setPixel(x,y,0)
                        continue
                        
                    # left half of upper row
                    if (y < p_y):
                        if (visible.pixel(x-1,y) == 0 or visible.pixel(x-1,y+1) == 0):
                            visible.setPixel(x,y,0)
                            continue
                    else:
                        if (visible.pixel(x-1,y) == 0 or visible.pixel(x-1,y-1) == 0):
                            visible.setPixel(x,y,0)
                            continue                    
                    # color point
                    img.setPixel(x,y,qRgb(qRed(img.pixel(x,y)),255,qBlue(img.pixel(x,y))))
                    #img.setPixel(x,y,qRgb(0,0,0))
                    visible2.setPixel(x,y,255)            