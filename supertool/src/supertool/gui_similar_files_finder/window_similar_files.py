import sys
from PyQt5 import QtWidgets
import gui_similar_files
import find_similar as finder


class MainApplication(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainApplication, self).__init__()

        self.ui = gui_similar_files.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.find_pressed)

    def find_pressed(self):
        path_to_directory = self.ui.textEdit.toPlainText()
        if path_to_directory:
            self.ui.listWidget.addItem('Results:')
            result = finder.find_similar(path_to_directory)
            for key, values in result.items():
                self.ui.listWidget.addItem('These files are the same with hash: {}'.format(key))
                for v in values:
                    self.ui.listWidget.addItem(v)
                self.ui.listWidget.addItem('')
        else:
            self.ui.listWidget.addItem("Please, try again! You have to enter the directory!")
        self.ui.listWidget.addItem("-" * 10)


app = QtWidgets.QApplication(sys.argv)
window = MainApplication()
window.show()

sys.exit(app.exec_())