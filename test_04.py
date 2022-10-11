#!/usr/bin/env python3


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QMessageBox

def on_button_clicked():
    alert = QMessageBox()
    alert.setText( 'you clicked it, not me!' )
    alert.exec()

app = QApplication( [] )

app.setStyleSheet( "QPushButton { margin: 10ex; }" )

window = QWidget(  ) 

layout = QVBoxLayout(  )
TopButton =  QPushButton( 'Top' ) 
layout.addWidget( TopButton )
BottomButton = QPushButton( 'Bottom' )
layout.addWidget( BottomButton )

TopButton.clicked.connect( on_button_clicked )
BottomButton.clicked.connect( on_button_clicked )

window.setLayout( layout )
window.show(  )

win2 = QWidget(  )
lay2 = QHBoxLayout(  )
lay2.addWidget( QPushButton( 'New Window' ) )
lay2.addWidget( QPushButton( 'New Layout' ) )
lay2.addWidget( QPushButton( 'New Button' ) )
win2.setLayout( lay2)
win2.show(  )

#app.setStyle('Windows')
palette = QPalette(  )
palette.setColor(  QPalette.ButtonText, Qt.red  )
app.setPalette(  palette )

app.exec()





