# Example from Pi Educational Manual v1.0 P. 94
# Provided under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

# Include the system and graphical user interface modules
import sys
from PySide.QtGui import *
class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow,self).__init__()
        # name the widget
        self.setWindowTitle('Window Events')
        # create a label (a bit of text)
        self.label = QLabel('Read Me', self)
        # create a button widget, position it and
# connect a function when it is clicked
        button = QPushButton('Push Me', self)
        button.clicked.connect(self.buttonClicked)
        # create a vertically orientated layout box 
# for the other widgets
        layout = QVBoxLayout(self)
        layout.addWidget(button)
        layout.addWidget(self.label)
        
# track the mouse
        self.setMouseTracking(True)
    def buttonClicked(self):
        """ Update the text when the button is clicked """
        self.label.setText("Clicked")
        
    def mouseMoveEvent(self, event):
        """ 
        Update the text when the (tracked) mouse moves over MyWindow
        """
        self.label.setText(str(event.x()) + "," + str(event.y()))
    
# start an application and create a widget for the window, 
# giving it a name
application = QApplication(sys.argv)
# construct a widget called MyWindow
widget = MyWindow()
# show the widget
widget.show()
# start the application so it can do things 
# with the widgets we've created
application.exec_()
