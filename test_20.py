import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# ninja stuff here!
import importlib

import vehic00 as vehicSim

def reloadVehicCode():
   importlib.reload( vehicSim )

def window():
   app = QApplication(sys.argv)
   win = QDialog()
   b1 = QPushButton(win)
   b1.setText("Button1")
   b1.move(50,20)
   b1.clicked.connect(b1_clicked)
   
   b2 = QPushButton(win)
   b2.setText("Button2")
   b2.move(50,50)
   b2.clicked.connect(b2_clicked)

   b3 = QPushButton(win)
   b3.setText("RunSim")
   b3.move(50,80)
   b3.clicked.connect( runSim )

   b4 = QPushButton(win)
   b4.setText("reload vehic code")
   b4.move(50,110)
   b4.clicked.connect( reloadVehicCode )

   
   win.setGeometry(100,100,400,100)

   win.setWindowTitle("PyQt5")
   win.show()
   sys.exit(app.exec_())

def b1_clicked():
   print ("Button 1 clicked")

def b2_clicked():
   print ("Button 2 clicked")

def runSim():
   vehicSim.run()
   
if __name__ == '__main__':
   window()


