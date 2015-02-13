from PyQt4 import QtCore, QtGui
import main

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = main.mainUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())