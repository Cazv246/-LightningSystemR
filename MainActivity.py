import sys
from PyQt5 import uic, QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QSplashScreen
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets

qtCreatorFile = "MainPage.ui" 


Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):

        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowState.WindowFullScreen)
        self.setWindowFlags(QtCore.Qt.WindowType.WindowMaximizeButtonHint)
        
        self.btnLucesAltasDS.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgLucesAltas))
        self.btnLucesMediasDS.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgLucesMedias))
        self.btnCerrar.clicked.connect(self.close)

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)

    # create the splash screen
    splash_pix = QtGui.QPixmap("splash.png")
    splash = QSplashScreen(splash_pix)
    splash.setWindowState(QtCore.Qt.WindowState.WindowFullScreen)
    splash.show()

    # create the main window
    window = MyApp()

    # simulate some initialization process
    for i in range(0, 100):
        app.processEvents()

    # finish the splash screen and show the main window
    splash.finish(window)
    window.show()
    sys.exit(app.exec_())
