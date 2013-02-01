#!/usr/bin/python

from PySide.QtCore import QUrl
from PySide.QtGui import QPushButton, QApplication
from PySide.QtDeclarative import QDeclarativeView

if __name__ == '__main__':

    app = QApplication([])
    view = QDeclarativeView()

    #ctxt = view.rootContext()
    #ctxt.setContextProperty("projects", dataList)

    url = QUrl('qml/mainwindow.qml')

    view.setSource(url)
    view.show()

    app.exec_()
