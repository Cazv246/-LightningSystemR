import sys
from PyQt5 import uic, QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets

qtCreatorFile = "MainPage.ui" 


Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        
        
        self.btnLucesAltasDS.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgLucesAltas))
        self.btnLucesMediasDS.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgLucesMedias))
    
        
        
   





if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()