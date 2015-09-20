#!/usr/bin/python

import subprocess
import mainDialogUI
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSlot
import sys
import refactoredRaster
import contextlib

def runProgram():
	app = QtGui.QApplication(sys.argv)

	default_input_file = ''
	force_std_out = False
	if len(sys.argv) == 2:
		default_input_file = sys.argv[1]
		force_std_out = True
	window = MyDialog(default_input_file, force_std_out)
	window.show()
	sys.exit(app.exec_())


class MyDialog(QtGui.QDialog):
	def __init__(self, default_input_file, force_std_out):
		QtGui.QDialog.__init__(self)

		self.ui = mainDialogUI.Ui_Dialog()
		self.ui.setupUi(self)

		self.ui.SpeedValue.setValue(refactoredRaster.DEFAULT_SPEED)
		self.ui.AccelValue.setValue(refactoredRaster.DEFAULT_ACCEL)
		self.ui.LaserPowerValue.setValue(refactoredRaster.DEFAULT_LASER_POWER)
		self.ui.BidirectionalRaster.setChecked(refactoredRaster.DEFAULT_BIDIRECTIONAL_RASTER)
		self.ui.OriginXValue.setValue(refactoredRaster.DEFAULT_ORIGIN_X)
		self.ui.OriginYValue.setValue(refactoredRaster.DEFAULT_ORIGIN_Y)
		self.ui.MirrorX.setChecked(refactoredRaster.DEFAULT_MIRROR_X)
		self.ui.MirrorY.setChecked(refactoredRaster.DEFAULT_MIRROR_Y)
		self.ui.KeepAspectRatio.setChecked(refactoredRaster.DEFAULT_KEEP_ASPECT_RATIO)
		self.ui.RasterWidthValue.setValue(refactoredRaster.DEFAULT_RASTER_W)
		self.ui.RasterHeightValue.setValue(refactoredRaster.DEFAULT_RASTER_H)
		self.ui.XDPIValue.setValue(refactoredRaster.DEFAULT_XDPI)
		self.ui.YDPIValue.setValue(refactoredRaster.DEFAULT_YDPI)

		self.handle_file_name(default_input_file)
		self.force_std_out = force_std_out
		if force_std_out:
			self.ui.OutputStdout.setChecked(True)
			self.ui.OutputStdout.setEnabled(False)
			self.ui.OutputFileButton.setEnabled(False)
			self.ui.OutputFileField.setEnabled(False)

		self.connect(self.ui.InputFileButton, QtCore.SIGNAL('clicked()'), self.onInputFileButton)
		self.connect(self.ui.OutputFileButton, QtCore.SIGNAL('clicked()'), self.onOutputFileButton)
		self.connect(self.ui.GoButton, QtCore.SIGNAL('clicked()'), self.onGoButton)
		self.connect(self.ui.OutputStdout, QtCore.SIGNAL('clicked(bool)'), self.onStdOutCheckbox)

	def onInputFileButton(self):
		fileName = QtGui.QFileDialog.getOpenFileName(self)
		self.handle_file_name(fileName)
	
	def handle_file_name(self, fileName):
		self.ui.InputFileField.setPlainText(fileName)
		if fileName:
			inputPix = QtGui.QPixmap(fileName)
			self.ui.PreviewView.setPixmap(inputPix)


	def onOutputFileButton(self):
		fileName = QtGui.QFileDialog.getSaveFileName(self)
		self.ui.OutputFileField.setPlainText(fileName)

	def onStdOutCheckbox(self, state):
		self.ui.OutputFileField.setEnabled(not state)
		self.ui.OutputFileButton.setEnabled(not state)
		
	def onGoButton(self):
		inputFileName = self.ui.InputFileField.toPlainText()
		if self.ui.OutputStdout.isChecked():
			outputFileName = '-'
		else:
			outputFileName = self.ui.OutputFileField.toPlainText()
		if inputFileName and outputFileName:
			inputPix = QtGui.QPixmap(inputFileName)
			self.ui.PreviewView.setPixmap(inputPix)
			
			with smart_open(outputFileName) as output:
				if self.ui.AdvancedModeCheckbox.isChecked():
					self.advancedCall(str(inputFileName), output)
				else:
					refactoredRaster.main(str(inputFileName), output, pause_on_every_line=False)
			outputPix = QtGui.QPixmap('actual.png')
			self.ui.OutputView.setPixmap(outputPix)
			if self.force_std_out:
				sys.exit(0)
		else:
			self.ui.OutputView.setText("You are missing file names")

	def advancedCall(self, inputFileName, output):
		refactoredRaster.main(inputFileName, output, 
			SPEED=float(self.ui.SpeedValue.value()),
			ACCEL=float(self.ui.AccelValue.value()), 
			laser_power=int(self.ui.LaserPowerValue.value()), 
			bidirectional_raster=bool(self.ui.BidirectionalRaster.isChecked()),
			origin_x=float(self.ui.OriginXValue.value()), 
			origin_y=float(self.ui.OriginYValue.value()), 
			origin_loc=str(self.ui.OriginLocationDrop.currentText()), 
			mirror_x=bool(self.ui.MirrorX.isChecked()), 
			mirror_y=bool(self.ui.MirrorY.isChecked()), 
			keep_aspect_ratio=bool(self.ui.KeepAspectRatio.isChecked()), 
			raster_w=float(self.ui.RasterWidthValue.value()), 
			raster_h=float(self.ui.RasterHeightValue.value()), 
			XDPI=float(self.ui.XDPIValue.value()), 
			YDPI=float(self.ui.YDPIValue.value()),
			pause_on_every_line=False
			)

@contextlib.contextmanager
def smart_open(filename=None):
	if filename and filename != '-':
		fh = open(filename, 'w')
	else:
		fh = sys.stdout

	try:
		yield fh
	finally:
		if fh is not sys.stdout:
			fh.close()

if __name__ == '__main__':
   runProgram()
