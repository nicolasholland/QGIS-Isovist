# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Isovist_dialog_base.ui'
#
# Created: Wed Apr  1 22:16:50 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_IsovistDialogBase(object):
    def setupUi(self, IsovistDialogBase):
        IsovistDialogBase.setObjectName(_fromUtf8("IsovistDialogBase"))
        IsovistDialogBase.resize(398, 300)
        self.button_box = QtGui.QDialogButtonBox(IsovistDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.chkActivate = QtGui.QCheckBox(IsovistDialogBase)
        self.chkActivate.setGeometry(QtCore.QRect(30, 240, 131, 41))
        self.chkActivate.setObjectName(_fromUtf8("chkActivate"))
        self.lineEdit = QtGui.QLineEdit(IsovistDialogBase)
        self.lineEdit.setGeometry(QtCore.QRect(120, 100, 171, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(IsovistDialogBase)
        self.label.setGeometry(QtCore.QRect(120, 50, 161, 51))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(IsovistDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), IsovistDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), IsovistDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(IsovistDialogBase)

    def retranslateUi(self, IsovistDialogBase):
        IsovistDialogBase.setWindowTitle(_translate("IsovistDialogBase", "Isovist", None))
        self.chkActivate.setText(_translate("IsovistDialogBase", "Display Isovist", None))
        self.label.setText(_translate("IsovistDialogBase", "Latitude and Longitude", None))

