# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Isovist
                                 A QGIS plugin
 Isovist
                              -------------------
        begin                : 2015-03-31
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Nicolas Holland
        email                : hollandn@informatik.uni-freiburg.de
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import qgis
from Isovist_dialog import IsovistDialog
import os.path

#import packages
from isoMeasurement import isoMeasurement
from computeIso import computeIso
from convert import convert_param
import csv




class Isovist:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface

        # MyCode
        # a reference to our map canvas
        self.canvas = self.iface.mapCanvas() #CHANGE
        # this QGIS tool emits as QgsPoint after each click on the map canvas
        #self.clickTool = QgsMapToolEmitPoint(self.canvas)

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'Isovist_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = IsovistDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Isovist')        
        self.toolbar = self.iface.addToolBar(u'Isovist')
        self.toolbar.setObjectName(u'Isovist')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('Isovist', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/Isovist/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Isovist'),
            callback=self.run,
            parent=self.iface.mainWindow())
    
        #example Code
        #result = QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
        #QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )

    def handleMouseDown(self, point, button):
        QMessageBox.information( self.iface.mainWindow(),"Info", "X,Y = %s,%s" % (str(point.x()),str(point.y())) )


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Isovist'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar
        
    def verifyinput(self):
        try:
            int(self.dlg.ScaleValue.text())
            int(self.dlg.ImgSizeValue_h.text())
            int(self.dlg.ImgSizeValue_v.text())
            int(self.dlg.IsoSizeValue.text())
            int(self.dlg.IllegalValue.text())
            int(self.dlg.EPSGValue.text())
        except:            
            return 1
        return 0
        
    def singleIsovist(self, latitude, longitude):
        # Settings        
        scale       = int(self.dlg.ScaleValue.text())
        imageSize_h = int(self.dlg.ImgSizeValue_h.text())
        imageSize_v = int(self.dlg.ImgSizeValue_v.text())
        isoSize     = int(self.dlg.IsoSizeValue.text())
        illegal     = int(self.dlg.IllegalValue.text())
        EPSG        = int(self.dlg.EPSGValue.text())

        # Convert Geocoordinates from geographic format to projected
        x,y = convert_param(longitude, latitude ,EPSG)

        # Jump to Coordinate
        rect = QgsRectangle(float(x)-scale,float(y)-scale,float(x)+scale,float(y)+scale)
        
        # create image
        img = QImage(QSize(imageSize_h , imageSize_v), QImage.Format_ARGB32_Premultiplied)
        visible = QImage(QSize(imageSize_h , imageSize_v), QImage.Format_ARGB32_Premultiplied)
        visible2 = QImage(QSize(imageSize_h , imageSize_v), QImage.Format_ARGB32_Premultiplied)
        
        # set image's background color
        color = QColor(255, 255, 255)
        img.fill(color.rgb())         
        
        # create painter
        p = QPainter()
        p.begin(img)
        p.setRenderHint(QPainter.Antialiasing)
        render = QgsMapRenderer()

        # set layer set
        layer = qgis.utils.iface.activeLayer()
        lst = [layer.id()]  # add ID of every layer
        render.setLayerSet(lst)

        # set extent            
        render.setExtent(rect)

        # set output size
        render.setOutputSize(img.size(), img.logicalDpiX())

        # do the rendering
        render.render(p)
        p.end()
            
        # Init Isovist
        for i in range(0,imageSize_h):
            for j in range(0,imageSize_v):
                visible.setPixel(i,j,255)
                visible2.setPixel(i,j,0)
                    
        # Point that is the center of the isovist
        p_x = imageSize_h/2
        p_y = imageSize_v/2
        img.setPixel(p_x,p_y,100)
        visible2.setPixel(p_x,p_y,255)
        
        
        # Compute Isovist
        computeIso(img, visible, visible2, p_x,p_y,isoSize, illegal, imageSize_h, imageSize_v)        

        # Save Isovist image
        img.save("%f %f.png"%(latitude,longitude),"png")
        
        # Compute isovists metrics
        Area,Perimeter,AreaPerimeterRatio,drift,mean_radial,std_dev,max_rad,min_rad = isoMeasurement(visible2,p_x,p_y,imageSize_h,imageSize_v)
        Dispersion = mean_radial-std_dev
        Circularity = (3.1415*mean_radial*mean_radial)/Area
        Variance =  std_dev*std_dev
        
        out = [latitude,longitude,Area,Perimeter,AreaPerimeterRatio,drift,mean_radial,std_dev,max_rad,min_rad,Dispersion,Circularity,Variance]
        
        print out
        return out        
        
 

    def run(self):
        """ Isovist Calculation """
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        
        if not result:
            return 1;
            
        if self.verifyinput():
            print "Input Error"
            return 1        
        
        # Single Isovist
        if not (self.dlg.chkActivate.checkState()):
            latitude    = float(self.dlg.LatValue.text())
            longitude   = float(self.dlg.LonValue.text())
            self.singleIsovist(latitude, longitude)
            
        # read file data
        else:
            # param
            inputFile = self.dlg.InputFileValue.text()
            outputFile = self.dlg.OutputFileValue.text()            
            
            data = csv.reader(open(inputFile,"rb") , delimiter=',')
            writer = csv.writer(open(outputFile,"wb"),delimiter=';')
            
            for row in data:
                # get coordinates                
                latitude    = float(row[0])
                longitude   = float(row[1])
                
                # compute isovist
                iso_data = self.singleIsovist(latitude, longitude)
                
                # save metrics
                writer.writerow(iso_data)