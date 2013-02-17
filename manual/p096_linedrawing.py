# Example from Pi Educational Manual v1.0 P. 96
# Provided under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

# Include the system, maths and graphical user interface modules
import sys, math
from PySide.QtGui import *
from PySide.QtCore import *
class SketchWindow(QWidget):
    def __init__(self, title, draw, size):
        super(SketchWindow, self).__init__()
        self.setWindowTitle(title)
        width, height = size
        self.setGeometry(60, 60, width, height)
        self.windowSize = size
        self.draw = draw
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        pen = QPen(Qt.yellow, 4)
        qp.setPen(pen)
        self.draw(qp, self.windowSize)
        qp.end()
# this draw function is not within the SketchWindow class
def drawSine(context, size):
    width, height = size
    points = []
    for x in range(width):
        angle = 5 * x * 2 * math.pi / width
        qpoint = QPoint(x, (height/2) * (1+math.sin(angle)) )
        points.append(qpoint)
    context.drawPolyline(points)
# create the application and widget and start it
application = QApplication(sys.argv)
widget = SketchWindow('Sine', drawSine, (320,200))
widget.show()
application.exec_()
