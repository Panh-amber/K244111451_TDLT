import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Ex130.ui.Ex130MainWindowEx import Ex130MainWindowEx


app = QApplication(sys.argv)
window = QMainWindow()
ui = Ex130MainWindowEx()
ui.setupUi(window)
ui.show_window()
sys.exit(app.exec())
