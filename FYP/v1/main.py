'''
Created on 29 Aug, 2014

@author: Mark Ang
'''

from PyQt4 import QtGui
import frontendMain

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = frontendMain.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())