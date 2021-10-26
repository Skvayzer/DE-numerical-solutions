import numpy as np
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton
from scipy.interpolate import interp1d

from Graph import Graph
from Tab import Tab
import math

class SolutionsTab(Tab):
    def __init__(self):
        super(SolutionsTab, self).__init__()

        self.methodsGraph = Graph()
        self.errors = Graph()

        self.euler.setChecked(True)
        self.exact.setChecked(True)

        checkboxes = QHBoxLayout()
        checkboxes.addWidget(self.exact)
        checkboxes.addWidget(self.euler)
        checkboxes.addWidget(self.improved_euler)
        checkboxes.addWidget(self.runge_kutta)

        self.Fchangebtn = QPushButton('Change function')
        # adding action to the button
        self.Fchangebtn.clicked.connect(self.change)
        self.Fchangebtn.setStyleSheet("color: black")

        col1 = QVBoxLayout()

        col1.addLayout(checkboxes)
        col1.addWidget(self.methodsGraph)
        col1.addWidget(self.errors)

        col2 = QVBoxLayout()
        col2.setContentsMargins(0,30,0,0)

        col2.addLayout(self.inputField("Function", self.function))
        col2.addLayout(self.inputField("Derivative", self.derivative))
        col2.addWidget(self.Fchangebtn)
        col2.addLayout(self.inputField("x0", self.x0))
        col2.addLayout(self.inputField("y0", self.y0))
        col2.addLayout(self.inputField("X", self.X))
        col2.addLayout(self.inputField("N", self.N))
        col2.addWidget(self.button)
        col2.addStretch()

        outer_layout = QHBoxLayout()
        outer_layout.addLayout(col1)
        outer_layout.addLayout(col2)

        self.setLayout(outer_layout)
        self.plot()

    def plot(self):
        self.methodsGraph.figure.clear()
        # create an axis
        ax = self.methodsGraph.figure.add_subplot(111)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.title.set_text("Numerical solutions")

        self.errors.figure.clear()
        # create an axis
        error_ax = self.errors.figure.add_subplot(111)
        error_ax.set_xlabel("x")
        error_ax.set_ylabel("value")
        error_ax.title.set_text("LTEs")


        x0 = float(self.x0.text())
        X = float(self.X.text())
        y0 = float(self.y0.text())
        N = int(self.N.text())
        h = (X - x0) / N

        interval = [x0, X]
        if self.checked[0]:
            # N linearly spaced numbers
            x = np.linspace(interval[0], interval[1], N)
            y = self.solution(x)

            cubic_interpolation_model = interp1d(x, y, kind="cubic")
            y = cubic_interpolation_model(x)

            # plot data
            ax.plot(x, y, 'm', label=self.method_names[0])
        for i in range(1,4):
            if(self.checked[i]):
                x = interval[0]
                y = self.solution(x)
                x_coords = []
                y_coords = []
                LTE_coords=[]
                while x <= interval[1]:
                    x_coords.append(x)
                    y_coords.append(y)
                    point = [x, y]
                    x = x + h
                    y = y + h * self.methods[i](point[0], point[1], h)
                    LTE = abs(y-self.solution(x))

                    LTE_coords.append(LTE)

                # N linearly spaced numbers
                x = np.linspace(interval[0], interval[1], N)

                error_ax.plot(x_coords, LTE_coords, '-ok',  markersize=2, linewidth=1, color= 'r' if i==1 else 'g' if i==2 else 'b', label=self.method_names[i])
                # plot data
                ax.plot(x_coords,y_coords, '-ok',  markersize=2, linewidth=1, color='r' if i==1 else 'g' if i==2 else 'b', label=self.method_names[i])
        ax.legend()
        error_ax.legend()
        # refresh canvas
        self.methodsGraph.canvas.draw()
        self.errors.canvas.draw()

    def change(self):
        def newD(x,y):
            return eval(self.derivative.text())
        def newF(x):
            return eval(self.function.text())
        self.f = newD
        self.solution = newF

        self.plot()
