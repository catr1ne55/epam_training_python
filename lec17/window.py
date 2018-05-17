"""
Simple calculator.

"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import buttons
import functools


class MainApplication(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainApplication, self).__init__()

        self.ui = buttons.Ui_MainWindow()
        self.ui.setupUi(self)

        self.number_1 = ''
        self.number_2 = ''
        self.operation = None

        for i in range(9):
            col = i % 3
            row = i // 3

            button = QtWidgets.QPushButton(self.ui.gridLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
            button.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(30)
            font.setBold(True)
            font.setWeight(75)
            button.setFont(font)
            button.setText(str(i + 1))
            button.setObjectName("button_{}".format(i))
            self.ui.gridLayout.addWidget(button, row, col, 1, 1)
            button.clicked.connect(functools.partial(self.button_pressed, i+1))

        self.ui.drop_button.clicked.connect(self.drop)
        self.ui.plus_button.clicked.connect(self.plus_pressed)
        self.ui.minus_button.clicked.connect(self.minus_pressed)
        self.ui.div_button.clicked.connect(self.div_pressed)
        self.ui.mul_button.clicked.connect(self.mul_pressed)
        self.ui.pow_button.clicked.connect(self.pow_pressed)
        self.ui.eq_button.clicked.connect(self.eq_pressed)

    def drop(self):
        """
        Clear display and reset all values.
        :return: None
        """
        self.ui.lcdNumber.display(0)
        self.number_1 = ''
        self.number_2 = ''
        self.operation = None

    def plus_pressed(self):
        """
        Set "+" operation.

        :return: None
        """
        if not self.operation:
            self.operation = lambda x, y: x + y
        else:
            if self.number_1 and self.number_2:
                self.calculate()
                self.operation = lambda x, y: x + y

    def minus_pressed(self):
        """
        Set "-" operation.

        :return: None
        """
        if not self.operation:
            self.operation = lambda x, y: x - y
        else:
            if self.number_1 and self.number_2:
                self.calculate()
                self.operation = lambda x, y: x - y

    def div_pressed(self):
        """
        Set "/" operation.

        :return: None
        """
        if not self.operation:
            self.operation = lambda x, y: x / y
        else:
            if self.number_1 and self.number_2:
                self.calculate()
                self.operation = lambda x, y: x / y

    def mul_pressed(self):
        """
        Set "*" operation.

        :return: None
        """
        if not self.operation:
            self.operation = lambda x, y: x * y
        else:
            if self.number_1 and self.number_2:
                self.calculate()
                self.operation = lambda x, y: x * y

    def pow_pressed(self):
        """
        Set "^" operation.

        :return: None
        """
        if not self.operation:
            self.operation = lambda x, y: x ** y
        else:
            if self.number_1 and self.number_2:
                self.calculate()
                self.operation = lambda x, y: x ** y

    def button_pressed(self, number):
        """
        Adds digit into a number and store it in number_1 or number_2.

        :param number: number on pressed button.
        :return: None.
        """
        if not self.operation:
            self.number_1 += str(number)
            self.ui.lcdNumber.display(float(self.number_1))
        elif self.operation:
            self.number_2 += str(number)
            self.ui.lcdNumber.display(float(self.number_2))
        else:
            self.number_1 = str(self.calculate())

    def calculate(self):
        """
        Makes calculations between two numbers.

        :return: None
        """
        self.number_1 = self.operation(float(self.number_1), float(self.number_2))
        self.ui.lcdNumber.display(self.number_1)
        self.number_2 = ''

    def eq_pressed(self):
        """
        Calculates when "=" is pressed.

        :return: None
        """
        if self.number_2:
            self.calculate()


app = QtWidgets.QApplication(sys.argv)
window = MainApplication()
window.show()

sys.exit(app.exec_())