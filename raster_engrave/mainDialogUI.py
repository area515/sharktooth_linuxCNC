# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainDialog.ui'
#
# Created: Sat Sep  5 16:23:11 2015
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(792, 609)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalWidget = QtGui.QWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setObjectName(_fromUtf8("horizontalWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.PreviewView = QtGui.QLabel(self.horizontalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PreviewView.sizePolicy().hasHeightForWidth())
        self.PreviewView.setSizePolicy(sizePolicy)
        self.PreviewView.setMinimumSize(QtCore.QSize(0, 100))
        self.PreviewView.setScaledContents(False)
        self.PreviewView.setObjectName(_fromUtf8("PreviewView"))
        self.horizontalLayout.addWidget(self.PreviewView)
        self.OutputView = QtGui.QLabel(self.horizontalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OutputView.sizePolicy().hasHeightForWidth())
        self.OutputView.setSizePolicy(sizePolicy)
        self.OutputView.setMinimumSize(QtCore.QSize(0, 100))
        self.OutputView.setScaledContents(False)
        self.OutputView.setObjectName(_fromUtf8("OutputView"))
        self.horizontalLayout.addWidget(self.OutputView)
        self.verticalLayout_2.addWidget(self.horizontalWidget)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.GoButton = QtGui.QPushButton(self.tab)
        self.GoButton.setMinimumSize(QtCore.QSize(0, 27))
        self.GoButton.setMaximumSize(QtCore.QSize(16777215, 27))
        self.GoButton.setObjectName(_fromUtf8("GoButton"))
        self.horizontalLayout_4.addWidget(self.GoButton)
        self.AdvancedModeCheckbox = QtGui.QCheckBox(self.tab)
        self.AdvancedModeCheckbox.setObjectName(_fromUtf8("AdvancedModeCheckbox"))
        self.horizontalLayout_4.addWidget(self.AdvancedModeCheckbox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalWidget1 = QtGui.QWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget1.sizePolicy().hasHeightForWidth())
        self.horizontalWidget1.setSizePolicy(sizePolicy)
        self.horizontalWidget1.setMinimumSize(QtCore.QSize(0, 27))
        self.horizontalWidget1.setMaximumSize(QtCore.QSize(16777215, 27))
        self.horizontalWidget1.setObjectName(_fromUtf8("horizontalWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.InputFileField = QtGui.QPlainTextEdit(self.horizontalWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputFileField.sizePolicy().hasHeightForWidth())
        self.InputFileField.setSizePolicy(sizePolicy)
        self.InputFileField.setMinimumSize(QtCore.QSize(10, 25))
        self.InputFileField.setMaximumSize(QtCore.QSize(16777215, 25))
        self.InputFileField.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.InputFileField.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.InputFileField.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.InputFileField.setObjectName(_fromUtf8("InputFileField"))
        self.horizontalLayout_2.addWidget(self.InputFileField)
        self.InputFileButton = QtGui.QPushButton(self.horizontalWidget1)
        self.InputFileButton.setObjectName(_fromUtf8("InputFileButton"))
        self.horizontalLayout_2.addWidget(self.InputFileButton)
        self.verticalLayout_2.addWidget(self.horizontalWidget1)
        self.horizontalWidget_2 = QtGui.QWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget_2.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_2.setSizePolicy(sizePolicy)
        self.horizontalWidget_2.setObjectName(_fromUtf8("horizontalWidget_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.OutputFileField = QtGui.QPlainTextEdit(self.horizontalWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OutputFileField.sizePolicy().hasHeightForWidth())
        self.OutputFileField.setSizePolicy(sizePolicy)
        self.OutputFileField.setMinimumSize(QtCore.QSize(0, 27))
        self.OutputFileField.setMaximumSize(QtCore.QSize(16777215, 27))
        self.OutputFileField.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.OutputFileField.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.OutputFileField.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.OutputFileField.setObjectName(_fromUtf8("OutputFileField"))
        self.horizontalLayout_3.addWidget(self.OutputFileField)
        self.OutputFileButton = QtGui.QPushButton(self.horizontalWidget_2)
        self.OutputFileButton.setObjectName(_fromUtf8("OutputFileButton"))
        self.horizontalLayout_3.addWidget(self.OutputFileButton)
        self.OutputStdout = QtGui.QCheckBox(self.horizontalWidget_2)
        self.OutputStdout.setObjectName(_fromUtf8("OutputStdout"))
        self.horizontalLayout_3.addWidget(self.OutputStdout)
        self.verticalLayout_2.addWidget(self.horizontalWidget_2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.Foo = QtGui.QVBoxLayout(self.tab_2)
        self.Foo.setObjectName(_fromUtf8("Foo"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.SpeedValue = QtGui.QDoubleSpinBox(self.tab_2)
        self.SpeedValue.setFrame(False)
        self.SpeedValue.setMaximum(200.0)
        self.SpeedValue.setObjectName(_fromUtf8("SpeedValue"))
        self.horizontalLayout_5.addWidget(self.SpeedValue)
        self.SpeedLabel = QtGui.QLabel(self.tab_2)
        self.SpeedLabel.setObjectName(_fromUtf8("SpeedLabel"))
        self.horizontalLayout_5.addWidget(self.SpeedLabel)
        self.Foo.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.AccelValue = QtGui.QDoubleSpinBox(self.tab_2)
        self.AccelValue.setFrame(False)
        self.AccelValue.setMaximum(200.0)
        self.AccelValue.setObjectName(_fromUtf8("AccelValue"))
        self.horizontalLayout_6.addWidget(self.AccelValue)
        self.AccelLabel = QtGui.QLabel(self.tab_2)
        self.AccelLabel.setObjectName(_fromUtf8("AccelLabel"))
        self.horizontalLayout_6.addWidget(self.AccelLabel)
        self.Foo.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.LaserPowerValue = QtGui.QSpinBox(self.tab_2)
        self.LaserPowerValue.setFrame(False)
        self.LaserPowerValue.setMaximum(150)
        self.LaserPowerValue.setObjectName(_fromUtf8("LaserPowerValue"))
        self.horizontalLayout_7.addWidget(self.LaserPowerValue)
        self.LaserPowerLabel = QtGui.QLabel(self.tab_2)
        self.LaserPowerLabel.setObjectName(_fromUtf8("LaserPowerLabel"))
        self.horizontalLayout_7.addWidget(self.LaserPowerLabel)
        self.Foo.addLayout(self.horizontalLayout_7)
        self.BidirectionalRaster = QtGui.QCheckBox(self.tab_2)
        self.BidirectionalRaster.setObjectName(_fromUtf8("BidirectionalRaster"))
        self.Foo.addWidget(self.BidirectionalRaster)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.OriginLocationDrop = QtGui.QComboBox(self.tab_2)
        self.OriginLocationDrop.setObjectName(_fromUtf8("OriginLocationDrop"))
        self.OriginLocationDrop.addItem(_fromUtf8(""))
        self.OriginLocationDrop.addItem(_fromUtf8(""))
        self.OriginLocationDrop.addItem(_fromUtf8(""))
        self.OriginLocationDrop.addItem(_fromUtf8(""))
        self.OriginLocationDrop.addItem(_fromUtf8(""))
        self.OriginLocationDrop.addItem(_fromUtf8(""))
        self.OriginLocationDrop.addItem(_fromUtf8(""))
        self.OriginLocationDrop.addItem(_fromUtf8(""))
        self.OriginLocationDrop.addItem(_fromUtf8(""))
        self.horizontalLayout_10.addWidget(self.OriginLocationDrop)
        self.OriginLocationLabel = QtGui.QLabel(self.tab_2)
        self.OriginLocationLabel.setObjectName(_fromUtf8("OriginLocationLabel"))
        self.horizontalLayout_10.addWidget(self.OriginLocationLabel)
        self.Foo.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.OriginXValue = QtGui.QDoubleSpinBox(self.tab_2)
        self.OriginXValue.setFrame(False)
        self.OriginXValue.setDecimals(5)
        self.OriginXValue.setObjectName(_fromUtf8("OriginXValue"))
        self.horizontalLayout_8.addWidget(self.OriginXValue)
        self.OriginXLabel = QtGui.QLabel(self.tab_2)
        self.OriginXLabel.setObjectName(_fromUtf8("OriginXLabel"))
        self.horizontalLayout_8.addWidget(self.OriginXLabel)
        self.Foo.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.OriginYValue = QtGui.QDoubleSpinBox(self.tab_2)
        self.OriginYValue.setFrame(False)
        self.OriginYValue.setDecimals(5)
        self.OriginYValue.setObjectName(_fromUtf8("OriginYValue"))
        self.horizontalLayout_9.addWidget(self.OriginYValue)
        self.OriginYLabel = QtGui.QLabel(self.tab_2)
        self.OriginYLabel.setObjectName(_fromUtf8("OriginYLabel"))
        self.horizontalLayout_9.addWidget(self.OriginYLabel)
        self.Foo.addLayout(self.horizontalLayout_9)
        self.MirrorX = QtGui.QCheckBox(self.tab_2)
        self.MirrorX.setObjectName(_fromUtf8("MirrorX"))
        self.Foo.addWidget(self.MirrorX)
        self.MirrorY = QtGui.QCheckBox(self.tab_2)
        self.MirrorY.setObjectName(_fromUtf8("MirrorY"))
        self.Foo.addWidget(self.MirrorY)
        self.KeepAspectRatio = QtGui.QCheckBox(self.tab_2)
        self.KeepAspectRatio.setObjectName(_fromUtf8("KeepAspectRatio"))
        self.Foo.addWidget(self.KeepAspectRatio)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.RasterWidthValue = QtGui.QDoubleSpinBox(self.tab_2)
        self.RasterWidthValue.setFrame(False)
        self.RasterWidthValue.setMinimum(-1.0)
        self.RasterWidthValue.setObjectName(_fromUtf8("RasterWidthValue"))
        self.horizontalLayout_11.addWidget(self.RasterWidthValue)
        self.RasterWidthLabel = QtGui.QLabel(self.tab_2)
        self.RasterWidthLabel.setObjectName(_fromUtf8("RasterWidthLabel"))
        self.horizontalLayout_11.addWidget(self.RasterWidthLabel)
        self.Foo.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.RasterHeightValue = QtGui.QDoubleSpinBox(self.tab_2)
        self.RasterHeightValue.setFrame(False)
        self.RasterHeightValue.setMinimum(-1.0)
        self.RasterHeightValue.setObjectName(_fromUtf8("RasterHeightValue"))
        self.horizontalLayout_14.addWidget(self.RasterHeightValue)
        self.RasterHeightLabel = QtGui.QLabel(self.tab_2)
        self.RasterHeightLabel.setObjectName(_fromUtf8("RasterHeightLabel"))
        self.horizontalLayout_14.addWidget(self.RasterHeightLabel)
        self.Foo.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.XDPIValue = QtGui.QSpinBox(self.tab_2)
        self.XDPIValue.setFrame(False)
        self.XDPIValue.setMaximum(300)
        self.XDPIValue.setObjectName(_fromUtf8("XDPIValue"))
        self.horizontalLayout_12.addWidget(self.XDPIValue)
        self.XDPILabel = QtGui.QLabel(self.tab_2)
        self.XDPILabel.setObjectName(_fromUtf8("XDPILabel"))
        self.horizontalLayout_12.addWidget(self.XDPILabel)
        self.Foo.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.YDPIValue = QtGui.QSpinBox(self.tab_2)
        self.YDPIValue.setFrame(False)
        self.YDPIValue.setMaximum(300)
        self.YDPIValue.setObjectName(_fromUtf8("YDPIValue"))
        self.horizontalLayout_13.addWidget(self.YDPIValue)
        self.YDPILabel = QtGui.QLabel(self.tab_2)
        self.YDPILabel.setObjectName(_fromUtf8("YDPILabel"))
        self.horizontalLayout_13.addWidget(self.YDPILabel)
        self.Foo.addLayout(self.horizontalLayout_13)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Ray\'s Fancy Raster Program", None, QtGui.QApplication.UnicodeUTF8))
        self.PreviewView.setText(QtGui.QApplication.translate("Dialog", "Preview Image", None, QtGui.QApplication.UnicodeUTF8))
        self.OutputView.setText(QtGui.QApplication.translate("Dialog", "Output Image", None, QtGui.QApplication.UnicodeUTF8))
        self.GoButton.setText(QtGui.QApplication.translate("Dialog", "Go Button", None, QtGui.QApplication.UnicodeUTF8))
        self.AdvancedModeCheckbox.setText(QtGui.QApplication.translate("Dialog", "Advanced Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.InputFileButton.setText(QtGui.QApplication.translate("Dialog", "Input File", None, QtGui.QApplication.UnicodeUTF8))
        self.OutputFileButton.setText(QtGui.QApplication.translate("Dialog", "Output File", None, QtGui.QApplication.UnicodeUTF8))
        self.OutputStdout.setText(QtGui.QApplication.translate("Dialog", "Std Out", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Dialog", "Basic Commands", None, QtGui.QApplication.UnicodeUTF8))
        self.SpeedLabel.setText(QtGui.QApplication.translate("Dialog", "Speed", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelLabel.setText(QtGui.QApplication.translate("Dialog", "Accel", None, QtGui.QApplication.UnicodeUTF8))
        self.LaserPowerLabel.setText(QtGui.QApplication.translate("Dialog", "Laser Power", None, QtGui.QApplication.UnicodeUTF8))
        self.BidirectionalRaster.setText(QtGui.QApplication.translate("Dialog", "Bidirectional Raster", None, QtGui.QApplication.UnicodeUTF8))
        self.OriginLocationDrop.setItemText(0, QtGui.QApplication.translate("Dialog", "bottom_left", None, QtGui.QApplication.UnicodeUTF8))
        self.OriginLocationDrop.setItemText(1, QtGui.QApplication.translate("Dialog", "bottom_center", None, QtGui.QApplication.UnicodeUTF8))
        self.OriginLocationDrop.setItemText(2, QtGui.QApplication.translate("Dialog", "bottom_right", None, QtGui.QApplication.UnicodeUTF8))
        self.OriginLocationDrop.setItemText(3, QtGui.QApplication.translate("Dialog", "middle_left", None, QtGui.QApplication.UnicodeUTF8))
        self.OriginLocationDrop.setItemText(4, QtGui.QApplication.translate("Dialog", "middle_center", None, QtGui.QApplication.UnicodeUTF8))
        self.OriginLocationDrop.setItemText(5, QtGui.QApplication.translate("Dialog", "middle_right", None, QtGui.QApplication.UnicodeUTF8))
        self.OriginLocationDrop.setItemText(6, QtGui.QApplication.translate("Dialog", "top_left", None, QtGui.QApplication.UnicodeUTF8))
        self.OriginLocationDrop.setItemText(7, QtGui.QApplication.translate("Dialog", "top_center", None, QtGui.QApplication.UnicodeUTF8))
        self.OriginLocationDrop.setItemText(8, QtGui.QApplication.translate("Dialog", "top_right", None, QtGui.QApplication.UnicodeUTF8))
        self.OriginLocationLabel.setText(QtGui.QApplication.translate("Dialog", "Origin Location", None, QtGui.QApplication.UnicodeUTF8))
        self.OriginXLabel.setText(QtGui.QApplication.translate("Dialog", "Origin X (in)", None, QtGui.QApplication.UnicodeUTF8))
        self.OriginYLabel.setText(QtGui.QApplication.translate("Dialog", "Origin Y (in)", None, QtGui.QApplication.UnicodeUTF8))
        self.MirrorX.setText(QtGui.QApplication.translate("Dialog", "Mirror X", None, QtGui.QApplication.UnicodeUTF8))
        self.MirrorY.setText(QtGui.QApplication.translate("Dialog", "Mirror Y", None, QtGui.QApplication.UnicodeUTF8))
        self.KeepAspectRatio.setText(QtGui.QApplication.translate("Dialog", "Keep Aspect Ratio", None, QtGui.QApplication.UnicodeUTF8))
        self.RasterWidthLabel.setText(QtGui.QApplication.translate("Dialog", "Raster Width (in)", None, QtGui.QApplication.UnicodeUTF8))
        self.RasterHeightLabel.setText(QtGui.QApplication.translate("Dialog", "Raster Height (in)", None, QtGui.QApplication.UnicodeUTF8))
        self.XDPILabel.setText(QtGui.QApplication.translate("Dialog", "XDPI", None, QtGui.QApplication.UnicodeUTF8))
        self.YDPILabel.setText(QtGui.QApplication.translate("Dialog", "YDPI", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Dialog", "Advanced Options", None, QtGui.QApplication.UnicodeUTF8))

