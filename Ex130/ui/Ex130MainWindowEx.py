import sys
from PyQt6.QtWidgets import QMessageBox

from Ex130.libs.my_module import tinh_khau_hao, tinh_chitiet_khau_hao
from Ex130.ui.Ex130MainWindow import Ui_MainWindow


class Ex130MainWindowEx(Ui_MainWindow):

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def show_window(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonTinhKhauHao.clicked.connect(self.tinh_khau_hao)
        self.pushButtonChiTietKhauHao.clicked.connect(self.chi_tiet_khau_hao)
        self.pushButtonXoa.clicked.connect(self.xoa_du_lieu)
        self.pushButtonThoat.clicked.connect(self.thoat)

    def dinh_dang_tien(self, so_tien):
        # Định dạng kiểu Việt Nam: 1.234.567
        return f"{so_tien:,.0f}".replace(",", ".")

    def doc_phi(self, text):
        # Không có phí vận chuyển / lắp đặt thì mặc định là 0
        text = text.strip()
        if text == "":
            return 0
        return float(text)

    def doc_du_lieu(self):
        # Trả về (giá mua, phí vận chuyển, phí lắp đặt, số năm); dữ liệu sai thì trả về None
        try:
            gia_mua = float(self.lineEditGiaMuaMoi.text().strip())
            phi_vanchuyen = self.doc_phi(self.lineEditPhiVanChuyen.text())
            chi_phi_lapdat = self.doc_phi(self.lineEditPhiLapDat.text())
            so_nam = int(self.lineEditSoNamDuKien.text().strip())

            if gia_mua <= 0 or phi_vanchuyen < 0 or chi_phi_lapdat < 0 or so_nam <= 0:
                QMessageBox.warning(
                    self.MainWindow,
                    "Lỗi dữ liệu",
                    "Giá mua và số năm phải lớn hơn 0, các loại phí không được âm!"
                )
                return None
            return gia_mua, phi_vanchuyen, chi_phi_lapdat, so_nam

        except ValueError:
            QMessageBox.critical(
                self.MainWindow,
                "Lỗi nhập liệu",
                "Vui lòng nhập số hợp lệ (số năm phải là số nguyên)!"
            )
            return None

    def tinh_khau_hao(self):
        du_lieu = self.doc_du_lieu()
        if du_lieu is None:
            return
        gia_mua, phi_vanchuyen, chi_phi_lapdat, so_nam = du_lieu
        nguyen_gia, khauhao_nam, khauhao_thang = tinh_khau_hao(
            gia_mua, phi_vanchuyen, chi_phi_lapdat, so_nam)
        self.lineEditNguyenGia.setText(self.dinh_dang_tien(nguyen_gia))
        self.lineEditKhauHaoNam.setText(self.dinh_dang_tien(khauhao_nam))
        self.lineEditKhauHaoThang.setText(self.dinh_dang_tien(khauhao_thang))

    def chi_tiet_khau_hao(self):
        du_lieu = self.doc_du_lieu()
        if du_lieu is None:
            return
        gia_mua, phi_vanchuyen, chi_phi_lapdat, so_nam = du_lieu
        chi_tiet = tinh_chitiet_khau_hao(gia_mua, phi_vanchuyen, chi_phi_lapdat, so_nam)
        self.textEditXemChiTiet.setPlainText(chi_tiet)

    def xoa_du_lieu(self):
        self.lineEditGiaMuaMoi.clear()
        self.lineEditPhiVanChuyen.setText("0")
        self.lineEditPhiLapDat.setText("0")
        self.lineEditSoNamDuKien.clear()
        self.lineEditNguyenGia.clear()
        self.lineEditKhauHaoNam.clear()
        self.lineEditKhauHaoThang.clear()
        self.textEditXemChiTiet.clear()
        self.lineEditGiaMuaMoi.setFocus()

    def thoat(self):
        msg = QMessageBox()
        msg.setWindowTitle("Xác nhận")
        msg.setText("Bạn có muốn thoát chương trình?")
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if msg.exec() == QMessageBox.StandardButton.Yes:
            sys.exit(0)
