import sys
from PyQt5 import uic, QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QSplashScreen
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO

qtCreatorFile = "MainPage.ui" 
GPIO.setmode(GPIO.BCM)


GPIO.setup(23, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

GPIO.output(23, GPIO.HIGH)
GPIO.output(16, GPIO.HIGH)
GPIO.output(25, GPIO.HIGH)
GPIO.output(6, GPIO.HIGH)
GPIO.output(5, GPIO.HIGH)
GPIO.output(24, GPIO.HIGH)
GPIO.output(19, GPIO.HIGH)
GPIO.output(26, GPIO.HIGH)
GPIO.output(20, GPIO.HIGH)
GPIO.output(13, GPIO.HIGH)
GPIO.output(27, GPIO.HIGH)
GPIO.output(22, GPIO.HIGH)



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
        self.btnDireccionalesDS.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgDireccionales))
        self.btnLucesBajasDS.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgLucesBajas))
        self.btnNeblinerosDS.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgNeblineros))
        self.btnDireccionalesDS.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgDireccionales))
        self.btnLuzEmergenciaDS.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgParqueo))
        self.btnLuzFrenoDS.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgFreno))
        self.btnLuzRetroDS.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgRetro))
        self.btnLuzSalonDS.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgSalon))
        self.btnPitoDS.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgPito))
        self.btnRadioDS.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgRadio))
        
        self.btnAltas2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgLucesAltas))
        self.btnMedias2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgLucesMedias))
        self.btnDireccionales2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgDireccionales))
        self.btnBajas2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgLucesBajas))
        self.btnNeblineros2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgNeblineros))
        self.btnDireccionales2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgDireccionales))
        self.btnParqueo2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgParqueo))
        self.btnFreno2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgFreno))
        self.btnRetro2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgRetro))
        self.btnSalon2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgSalon))
        self.btnPito2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgPito))
        self.btnRadio2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pgRadio))
        
        
        
        
        self.btnInfoMedias.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.infoMedias))
        self.btnInfoLucesBajas.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.infoBajas))
        self.btnInfoLucesAltas.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.infoAltas))
        self.btnInfoNeblineros.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.infoNeblineros))
        self.btnInfoDireccionales.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.infoDireccionales))
        self.btnInfoParqueo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.infoParqueo))
        self.btnInfoFreno.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.infoFreno))
        self.btnInfoRetro.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.infoRetro))
        self.btnInfoSalon.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.infoLuzSalon))
        self.btnInfoPito.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.infoPito))
        self.btnInfoRadio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.infoRadio))
        


        self.btnLucesMedias.clicked.connect(self.LucesMedias)
        self.btnLucesAltas.clicked.connect(self.LucesAltas)
        self.btnLucesBajas.clicked.connect(self.LucesBajas)
        self.btnNeblineros.clicked.connect(self.Neblineros)
        self.btnLeft.clicked.connect(self.DireIzquierda)
        self.btnRight.clicked.connect(self.DireDerecha)
        self.btnParqueo.clicked.connect(self.Parqueo)
        self.btnFreno.clicked.connect(self.Freno)
        self.btnRetro.clicked.connect(self.Retro)
        self.btnSalon.clicked.connect(self.Salon)
        self.btnPito.clicked.connect(self.Pito)
        self.btnRadio.clicked.connect(self.Radio)
        
        
        
        
        
        
        self.btnCerrar.clicked.connect(self.close)

    def Radio(self):
        if GPIO.input(22):
            GPIO.output(22, GPIO.LOW)
            self.SonidoR1.setEnabled(True)
            self.SonidoR2.setEnabled(True)
            self.btnRadio.setText("APAGAR")
        else:
            GPIO.output(22, GPIO.HIGH)
            self.SonidoR1.setEnabled(False)
            self.SonidoR2.setEnabled(False)
            self.btnRadio.setText("ENCENDER")  


    def Pito(self):
        if GPIO.input(27):
            GPIO.output(27, GPIO.LOW)
            self.SonidoP1.setEnabled(True)
            self.btnPito.setText("APAGAR")
        else:
            GPIO.output(27, GPIO.HIGH)
            self.SonidoP1.setEnabled(False)
            self.btnPito.setText("ENCENDER")  

    def Salon(self):
        
        if GPIO.input(20):
            GPIO.output(20, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            self.focoS1.setEnabled(True)
            self.btnSalon.setText("APAGAR")
        else:
            GPIO.output(20, GPIO.HIGH)
            GPIO.output(13, GPIO.HIGH)
            self.focoS1.setEnabled(False)
            self.btnSalon.setText("ENCENDER")

    def Retro(self):
        if GPIO.input(26):
            GPIO.output(26, GPIO.LOW)
            self.focoR1.setEnabled(True)
            self.focoR2.setEnabled(True)
            self.btnRetro.setText("APAGAR")
        else:
            GPIO.output(26, GPIO.HIGH)
            self.focoR1.setEnabled(False)
            self.focoR2.setEnabled(False)
            
            self.btnRetro.setText("ENCENDER") 

    def Freno(self):
        if GPIO.input(19):
            GPIO.output(19, GPIO.LOW)
            self.focoF1.setEnabled(True)
            self.focoF2.setEnabled(True)
            self.focoF3.setEnabled(True)
            self.focoF4.setEnabled(True)

            self.btnFreno.setText("APAGAR")
        else:
            GPIO.output(19, GPIO.HIGH)
            self.focoF1.setEnabled(False)
            self.focoF2.setEnabled(False)
            self.focoF3.setEnabled(False)
            self.focoF4.setEnabled(False)
            self.btnFreno.setText("ENCENDER")  

    def DireIzquierda(self):
        if GPIO.input(5):
            GPIO.output(5, GPIO.LOW)
            GPIO.output(24, GPIO.HIGH)
            self.focoD1.setEnabled(True)
            self.focoD1_1.setEnabled(True)
            self.focoD2.setEnabled(False)
            self.focoD2_2.setEnabled(False)
            self.btnRight.setText("ENCENDER")
            self.btnLeft.setText("APAGAR")
        else:
            GPIO.output(5, GPIO.HIGH)
            self.focoD1.setEnabled(False)
            self.focoD1_1.setEnabled(False)
            self.btnLeft.setText("ENCENDER")

    def DireDerecha(self):
        if GPIO.input(24):
            GPIO.output(24, GPIO.LOW)
            GPIO.output(5, GPIO.HIGH)
            self.focoD1.setEnabled(False)
            self.focoD1_1.setEnabled(False)
            self.focoD2.setEnabled(True)
            self.focoD2_2.setEnabled(True)
            self.btnLeft.setText("ENCENDER")
            self.btnRight.setText("APAGAR")
        else:
            GPIO.output(24, GPIO.HIGH)
            self.focoD2.setEnabled(False)
            self.focoD2_2.setEnabled(False)
            self.btnRight.setText("ENCENDER")
        
    def Parqueo(self):
        
        if GPIO.input(24):
            GPIO.output(24, GPIO.LOW)
            GPIO.output(5, GPIO.LOW)
            self.focoP1.setEnabled(True)
            self.focoP2.setEnabled(True)
            self.focoP3.setEnabled(True)
            self.focoP4.setEnabled(True)

            
            self.btnParqueo.setText("APAGAR")
        else:
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(5, GPIO.HIGH)
            self.focoP1.setEnabled(False)
            self.focoP2.setEnabled(False)
            self.focoP3.setEnabled(False)
            self.focoP4.setEnabled(False)
            
            self.btnParqueo.setText("ENCENDER")


    def LucesMedias(self):
        if GPIO.input(23):
            GPIO.output(23, GPIO.LOW)
            self.focoM1.setEnabled(True)
            self.focoM2.setEnabled(True)
            self.focoM3.setEnabled(True)
            self.focoM4.setEnabled(True)
            self.focoM5.setEnabled(True)
            self.focoM6.setEnabled(True)
            self.btnLucesMedias.setText("APAGAR")
        else:
            GPIO.output(23, GPIO.HIGH)
            self.focoM1.setEnabled(False)
            self.focoM2.setEnabled(False)
            self.focoM3.setEnabled(False)
            self.focoM4.setEnabled(False)
            self.focoM5.setEnabled(False)
            self.focoM6.setEnabled(False)
            self.btnLucesMedias.setText("ENCENDER")

    def LucesBajas(self):
        if GPIO.input(16):
            GPIO.output(16, GPIO.LOW)
            self.focoB1.setEnabled(True)
            self.focoB2.setEnabled(True)
            self.btnLucesBajas.setText("APAGAR")
        else:
            GPIO.output(16, GPIO.HIGH)
            self.focoB1.setEnabled(False)
            self.focoB2.setEnabled(False)
            self.btnLucesBajas.setText("ENCENDER")

    def LucesAltas(self):
        if GPIO.input(25):
            GPIO.output(25, GPIO.LOW)
            self.focoA1.setEnabled(True)
            self.focoA2.setEnabled(True)
            self.btnLucesAltas.setText("APAGAR")
        else:
            GPIO.output(25, GPIO.HIGH)
            self.focoA1.setEnabled(False)
            self.focoA2.setEnabled(False)
            self.btnLucesAltas.setText("ENCENDER")

    def Neblineros(self):
        if GPIO.input(6):
            GPIO.output(6, GPIO.LOW)
            self.focoN1.setEnabled(True)
            self.focoN2.setEnabled(True)
            self.btnNeblineros.setText("APAGAR")
        else:
            GPIO.output(6, GPIO.HIGH)
            self.focoN1.setEnabled(False)
            self.focoN2.setEnabled(False)
            self.btnNeblineros.setText("ENCENDER")
        


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
