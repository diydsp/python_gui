#!/usr/bin/env python3


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout

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

app.exec()




