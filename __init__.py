# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Isovist
                                 A QGIS plugin
 Isovist
                             -------------------
        begin                : 2015-03-31
        copyright            : (C) 2015 by Nicolas Holland
        email                : hollandn@informatik.uni-freiburg.de
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Isovist class from file Isovist.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Isovist import Isovist
    return Isovist(iface)
