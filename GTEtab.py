import numpy as np
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from scipy.interpolate import interp1d

from Graph import Graph
from Tab import Tab


class GTEtab(Tab):
    def __init__(self, solutions):
        super(GTEtab, self).__init__()
        self.GTEs = Graph()
        self.solutions = solutions

        self.euler.setChecked(True)
        self.exact.setChecked(True)

        checkboxes = QHBoxLayout()
        checkboxes.addWidget(self.euler)
        checkboxes.addWidget(self.improved_euler)
        checkboxes.addWidget(self.runge_kutta)
        self.exact.hide()

        col1 = QVBoxLayout()
        col1.addLayout(checkboxes)
        col1.addWidget(self.GTEs)

        col2 = QVBoxLayout()
        col2.setContentsMargins(0,30,0,0)
        col2.addLayout(self.inputField("n0", self.N0))
        col2.addLayout(self.inputField("N", self.N))
        col2.addWidget(self.button)
        col2.addStretch()

        outer_layout = QHBoxLayout()
        outer_layout.addLayout(col1)
        outer_layout.addLayout(col2)

        self.setLayout(outer_layout)
        self.plot()

    def plot(self):
        self.GTEs.figure.clear()
        # self.N.setText(self.solutions.N.text())

        self.solution = self.solutions.solution
        self.f = self.solutions.f
        # create an axis
        ax = self.GTEs.figure.add_subplot(111)
        ax.set_xlabel("x")
        ax.set_ylabel("E")
        ax.title.set_text("GTEs")

        x0 = float(self.solutions.x0.text())
        X = float(self.solutions.X.text())
        y0 = float(self.solutions.y0.text())
        N0 = int(self.N0.text())
        # self.solutions.N.setText(self.N.text())
        N = int(self.N.text())


        interval = [x0, X]

        for i in range(1,4):
            if(self.checked[i]):
                GTEs=[]
                for n in range(N0, N+1):
                    x = interval[0]
                    y = y0
                    maxLTE = 0
                    h = (X - x0) / n

                    while x <= interval[1]:
                        point = [x, y]
                        x = x + h
                        y = y + h * self.methods[i](point[0], point[1], h)
                        LTE = self.solution(x) - self.solution(point[0]) - h * self.methods[i](point[0], self.solution(point[0]), h)
                        if LTE > maxLTE:
                            maxLTE = LTE
                    GTEs.append(maxLTE)

                # N linearly spaced numbers
                x = np.linspace(N0, N, N-N0+1)

                cubic_interpolation_model = interp1d(x, GTEs, kind="cubic")
                y = cubic_interpolation_model(x)

                # plot data
                ax.plot(x,y, '-ok',  markersize=2, linewidth=1, color='r' if i==1 else 'g' if i==2 else 'b', label=self.method_names[i])
        ax.legend()
        # refresh canvas
        self.GTEs.canvas.draw()


