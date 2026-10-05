import sys
from PyQt6.QtWidgets import QMessageBox

from Ex82.libs.my_module import calc_electricity_bill
from Ex82.ui.Ex82MainWindow import Ui_MainWindow


class ex82MainWindowEx(Ui_MainWindow):

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def show_window(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_calc.clicked.connect(self.process_calc)
        self.pushButton_clear.clicked.connect(self.process_clear)
        self.pushButton_exit.clicked.connect(self.process_exit)

    def process_calc(self):
        try:
            name = self.customerNameLineEdit.text().strip()
            kwh_text = self.kwhLineEdit.text().strip()

            if not name or not kwh_text:
                raise ValueError("Chưa nhập đủ thông tin!")

            kwh = float(kwh_text)
            if kwh < 0:
                QMessageBox.warning(
                    self.MainWindow,
                    "Lỗi dữ liệu",
                    "Số kWh phải lớn hơn hoặc bằng 0!"
                )
                return

            group = self.customerGroupComboBox.currentIndex()
            total = calc_electricity_bill(group, kwh)

            # Định dạng kiểu Việt Nam: 1.234.567
            self.amountLineEdit.setText(f"{total:,.0f}".replace(",", "."))

        except ValueError:
            QMessageBox.critical(
                self.MainWindow,
                "Lỗi nhập liệu",
                "Vui lòng nhập tên khách hàng và số kWh hợp lệ (chỉ nhập số)!"
            )
            self.amountLineEdit.clear()

    def process_clear(self):
        self.customerNameLineEdit.clear()
        self.kwhLineEdit.clear()
        self.amountLineEdit.clear()
        self.customerGroupComboBox.setCurrentIndex(0)
        self.customerNameLineEdit.setFocus()

    def process_exit(self):
        msg = QMessageBox()
        msg.setWindowTitle("Xác nhận")
        msg.setText("Bạn có muốn thoát chương trình?")
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if msg.exec() == QMessageBox.StandardButton.Yes:
            sys.exit(0)
