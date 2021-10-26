import math

import numpy as np
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QCheckBox, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox
from scipy.interpolate import interp1d

from Graph import Graph


class Tab(QWidget):
    def __init__(self):
        super(Tab, self).__init__()

        self.methods = [self.solution, self.Euler, self.ImprovedEuler, self.RungeKutta]
        self.method_names=['Exact', 'Euler', 'improved Euler', 'Runge-Kutta']
        self.checked = [True, True, False, False]
        self.poins_of_discontinuity_list=[]

        # Just some button connected to 'plot' method
        self.button = QPushButton('Plot')
        # adding action to the button
        self.button.clicked.connect(self.clickBtn)
        self.button.setStyleSheet("color: black")

        self.x0 = QLineEdit()
        self.x0.setText(str(round(math.pi, 4)))
        self.X = QLineEdit()
        self.X.setText(str(round(5*math.pi, 4)))
        self.y0 = QLineEdit()
        self.y0.setText("2")
        self.N0 = QLineEdit()
        self.N0.setText("10")
        self.N = QLineEdit()
        self.N.setText("100")
        self.function = QLineEdit()
        self.function.setText("(np.sin(x) ** 2 + 2 ** (3 / 2) * math.pi * np.sin(x) + 2 * math.pi ** 2) / x ** 2")
        self.derivative = QLineEdit()
        self.derivative.setText("2 * y ** (1 / 2) * np.cos(x) / x - 2 * y / x")
        self.points_of_discontinuity_field = QLineEdit()
        self.points_of_discontinuity_field.setText("0")
        self.exact = QCheckBox("Exact", self)
        self.exact.stateChanged.connect(self.clickBox)
        self.euler = QCheckBox("Euler", self)
        self.euler.stateChanged.connect(self.clickBox)
        self.improved_euler = QCheckBox("Improved Euler", self)
        self.improved_euler.stateChanged.connect(self.clickBox)
        self.runge_kutta = QCheckBox("Runge-Kutta", self)
        self.runge_kutta.stateChanged.connect(self.clickBox)

    def inputField(self, text, lineEdit):
        field = QHBoxLayout()
        label = QLabel()
        label.setText(text)
        label.setStyleSheet("color: rgb(50, 50, 50)")
        lineEdit.setStyleSheet("color: black")
        field.addWidget(label)
        field.addWidget(lineEdit)
        return field

    def plot(self):
       pass

    def clickBtn(self):
        x0 = float(self.x0.text())
        X = float(self.X.text())
        N = int(self.N.text())
        h = (X - x0) / N
        if h>1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Warning")
            msg.setStyleSheet("color: white")
            msg.setInformativeText('h = (X - x0) / N \nshould be greater than 1 for the methods to work correctly')
            msg.setWindowTitle("Warning")
            msg.exec_()
        self.plot()

    def clickBox(self):
        self.checked = [self.exact.isChecked(), self.euler.isChecked(), self.improved_euler.isChecked(), self.runge_kutta.isChecked()]
        self.plot()

    def f(self, x, y):
        return 2 * y ** (1 / 2) * np.cos(x) / x - 2 * y / x

    def solution(self, x):
        return (np.sin(x) ** 2 + 2 ** (3 / 2) * math.pi * np.sin(x) + 2 * math.pi ** 2) / x ** 2

    def Euler(self, x, y, h):
        return self.f(x, y)

    def ImprovedEuler(self, x, y, h):
        return self.f(x + h / 2, y + h * self.f(x, y) / 2)

    def RungeKutta(self, x, y, h):
        k1 = self.f(x, y)
        k2 = self.f(x + h / 2, y + h * k1 / 2)
        k3 = self.f(x + h / 2, y + h * k2 / 2)
        k4 = self.f(x + h, y + h * k3)
        return (k1 + 2 * k2 + 2 * k3 + k4) / 6
