from math import isfinite

from Chapter5.Ex73.libs.my_modules import solve_quadratic_equation
from Chapter5.Ex73.ui.MyMainWindow import Ui_MainWindow


class MyMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def show_window(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton.clicked.connect(self.solve_equation)

    def solve_equation(self):
        try:
            a = float(self.aLineEdit.text())
            b = float(self.bLineEdit.text())
            c = float(self.cLineEdit.text())
            if not all(isfinite(value) for value in (a, b, c)):
                raise ValueError
        except ValueError:
            self.resultLineEdit.setText("Please enter valid numbers for a, b and c")
            return
        result = solve_quadratic_equation(a, b, c)
        self.resultLineEdit.setText(result)
