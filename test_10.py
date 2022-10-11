#!/usr/bin/env python3


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



def window():
    app = QApplication( sys.argv )
    w = QWidget()
    b = QLabel( w )
    b.setText( "hello world" )
    w.setGeometry( 100, 100, 200, 50 )
    b.move(50,20)
    w.setWindowTitle("PyQt5 FTW!")
    w.show()

    sys.exit( app.exec_() )


if __name__ == '__main__':
    window()
    
