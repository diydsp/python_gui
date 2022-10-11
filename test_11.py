#!/usr/bin/env python3


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



def window( QWidget ):

    def __init__( self, parent = None ):
        super( window, self).__init__( parent )
        self.resize( 200, 50 )
        self.setWindowTitle("PyQt5 FTW!")
        self.label = QLabel( self )
        self.label.setText( "hello world" )

        font = QFont()
        font.setFamily( "Arial" )
        font.setPointSize( 16 )
        self.label.setFont( font )
        self.label.move( 50, 20 )

        return self
    
def main():
    app = QApplication( sys.argv )
    qw = QWidget()
    ex = window( qw )
    ex.show()
    sys.exit( app.exec_() )
    
if __name__ == '__main__':
    main()
