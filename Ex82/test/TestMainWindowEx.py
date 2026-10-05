import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Ex82.ui.Ex82MainWindowEx import ex82MainWindowEx


app = QApplication(sys.argv)
window = QMainWindow()
ui = ex82MainWindowEx()
ui.setupUi(window)
ui.show_window()
sys.exit(app.exec())
