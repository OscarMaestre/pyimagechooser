#!/usr/bin/env python3
#coding=utf-8

import sys

from PySide.QtCore import *
from PySide.QtGui import *

import MainWindow

class VentanaPrincipal (QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        self.STATUS_BAR_TIME=4000
        super(VentanaPrincipal, self).__init__(parent)
        self.setupUi(self)
        
        self.btnSelectRootFolder.clicked.connect( self.onSelectRootFolder )
        self.btnSelectFolder1.clicked.connect ( self.onSelectFolder1 )
        self.btnSelectFolder2.clicked.connect ( self.onSelectFolder2 )
        
        self.btnMoveToFolder1.clicked.connect ( self.onPressSendToFolder1 )
        self.btnMoveToFolder2.clicked.connect ( self.onPressSendToFolder2 )
        
        self.rootFolder=""
        self.folder1=""
        self.folder2=""
    
    def onSelectRootFolder(self):
        folder=QFileDialog.getExistingDirectory()
        msg="Selected root folder:{0}".format(folder)
        self.statusBar.showMessage(msg, self.STATUS_BAR_TIME)
        self.rootFolder=folder
        self.lblRootFolder.setText(folder)
        
        
    def onSelectFolder1(self):
        folder=QFileDialog.getExistingDirectory()
        msg="Selected folder 1:{0}".format(folder)
        self.statusBar.showMessage(msg, self.STATUS_BAR_TIME)
        self.folder1=folder
        self.lblFolder1.setText(folder)
        
    def onSelectFolder2(self):
        folder=QFileDialog.getExistingDirectory()
        msg="Selected folder 2:{0}".format(folder)
        self.statusBar.showMessage(msg, self.STATUS_BAR_TIME)
        self.folder2=folder
        self.lblFolder2.setText(folder)
        
    def onPressSendToFolder1(self):
        self.sendToFolder ( self.folder1 )
    
    def onPressSendToFolder2(self):
        self.sendToFolder ( self.folder2 )
    
    def sendToFolder(self, destination_folder):
        print ("Sending to "+destination_folder)
        
if __name__ == '__main__':
    app=QApplication (sys.argv)
    v=VentanaPrincipal()
    v.show()
    app.exec_()
    sys.exit()