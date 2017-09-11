import sys
import random

import time

from partikel_qt_res import *


class MeinDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.gs = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.gs)
        self.ctimer = QtCore.QTimer()
        self.ctimer.start(1)
        self.ctimer.timeout.connect(self.constantUpdate)
        self.oldi=0
        self.oldj=0

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        pen = QtGui.QPen(QtCore.Qt.yellow, 4)
        qp.setPen(pen)
        i = random.randrange(1, 200)
        j = random.randrange(1, 200)

        #self.gs.addEllipse(self.oldi, self.oldj, self.oldi, self.oldj, QtGui.QPen(QtCore.Qt.white, 3), QtGui.QBrush(QtCore.Qt.white))
        self.gs.addEllipse(i, j, i, j, QtGui.QPen(QtCore.Qt.darkYellow, 3), QtGui.QBrush(QtCore.Qt.red))
        qp.end()
        self.oldi = i
        self.oldj = j
        time.sleep(0.5)

    def constantUpdate(self):
        self.update()


app = QtWidgets.QApplication(sys.argv)
dialog = MeinDialog()
dialog.show()
sys.exit(app.exec_())