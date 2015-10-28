# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:17:58 2015

@author: dutchman
"""

import ogr, osr


def convert_param(x,y,inputEPSG):
    #pointX,pointY = 1286755.3, 6130409.7
    pointX,pointY = x,y
    

    # Spatial Reference System
    #inputEPSG = 3857
    #outputEPSG = 4326
    outputEPSG = 3857

    # create a geometry from coordinates
    point = ogr.Geometry(ogr.wkbPoint)
    point.AddPoint(pointX, pointY)

    # create coordinate transformation
    inSpatialRef = osr.SpatialReference()
    inSpatialRef.ImportFromEPSG(inputEPSG)

    outSpatialRef = osr.SpatialReference()
    outSpatialRef.ImportFromEPSG(outputEPSG)

    coordTransform = osr.CoordinateTransformation(inSpatialRef, outSpatialRef)

    # transform point
    point.Transform(coordTransform)

    # print point in EPSG 4326
    return point.GetX(), point.GetY()    