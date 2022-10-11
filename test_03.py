#!/usr/bin/env python3


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette

app = QApplication( [] )

window = QWidget(  ) 

layout = QVBoxLayout(  )
layout.addWidget( QPushButton( 'Top' ) )
layout.addWidget( QPushButton( 'Bottom' ) )

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





