import sys
from PyQt5.QtWidgets import (
    QApplication,
)
from GUI import GUI


# driver code
if __name__ == '__main__':
    # creating apyqt5 application
    app = QApplication(sys.argv)

    # creating a GUI object
    main = GUI()

    # showing the GUI
    main.show()

    # loop
    sys.exit(app.exec_())
