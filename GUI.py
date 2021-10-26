from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout

from GTEtab import GTEtab
from SolutionsTab import SolutionsTab


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(1000, 800))

        tab1 = SolutionsTab()
        tab2 = GTEtab(tab1)

        self.tabwidget = QTabWidget()
        self.tabwidget.setStyleSheet("color: black")

        self.tabwidget.currentChanged.connect(self.changeTab)
        self.tabwidget.addTab(tab1, "Solutions")
        self.tabwidget.addTab(tab2, "GTEs")

        self.setStyleSheet("background-color:white;")

        # setting layout to the main GUI
        outer_layout = QVBoxLayout()
        outer_layout.addWidget(self.tabwidget)
        self.setLayout(outer_layout)
    def changeTab(self):
        self.tabwidget.currentWidget().plot()