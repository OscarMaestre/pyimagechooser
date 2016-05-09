#!/usr/bin/env python3
#coding=utf-8

import sys, glob, os

from PySide.QtCore import *
from PySide.QtGui import *

import MainWindow

img_extensions=["*.jpg",  "*.gif", "*.png", "*.bmp", "*.jpeg"]

class ImagesFolder(object):
    def __init__(self, img_folder):
        self.path=img_folder
        self.files=[]
        for ext in img_extensions:
            self.files+=glob.glob(img_folder+ os.sep + ext)
        self.files.sort()
        #print (self.files)
        self.current_img=0
        
    def image_list_empty(self):
        if len(self.files)==0:
            print("Empty folder")
            return True
        print ("Folder with img")
        return False
    
    def get_image_list(self):
        file_list=[]
        for f in self.files:
            file_list.append ( os.path.basename(f))
        return file_list
    
    def current_image_index(self):
        return self.current_img
    
    def current_image_filename(self):
        return self.files [ self.current_img ]
    
    def folder_completely_processed(self):
        if self.current_img==len(self.files):
            return True
        return False
    
    def goto_next_image(self):
        if self.current_img < len ( self.files ):
            self.current_img+=1
        
class AppWindow (QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        self.STATUS_BAR_TIME=4000
        super(AppWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.btnSelectRootFolder.clicked.connect( self.onSelectRootFolder )
        self.btnSelectFolder1.clicked.connect ( self.onSelectFolder1 )
        self.btnSelectFolder2.clicked.connect ( self.onSelectFolder2 )
        
        self.btnMoveToFolder1.clicked.connect ( self.onPressSendToFolder1 )
        self.btnMoveToFolder2.clicked.connect ( self.onPressSendToFolder2 )
        
        self.rootFolder=""
        self.folder1=""
        self.folder2=""
        self.img_folder=None
        self.image_to_process=None
    
    def onSelectRootFolder(self):
        folder=QFileDialog.getExistingDirectory()
        msg="Selected root folder:{0}".format(folder)
        self.statusBar.showMessage(msg, self.STATUS_BAR_TIME)
        self.rootFolder=folder
        self.lblRootFolder.setText(folder)
        self.img_folder=ImagesFolder(folder)
        #Fill the QListWidget with the images in the selected folder
        if not self.img_folder.image_list_empty():
            for f in self.img_folder.get_image_list():
                self.lvImages.addItem(f)
            self.lvImages.setCurrentRow( 0 )
            self.image_to_process=QPixmap( self.img_folder.current_image_filename() )
            self.lblImagePreview.setPixmap( self.image_to_process )
            
        
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
    w=AppWindow()
    w.show()
    app.exec_()
    sys.exit()