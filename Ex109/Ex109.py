def tinh_nguyen_gia(gia_goc, phi_van_chuyen, phi_lap_dat):
    # Nguyên giá TSCĐ = giá mua + phí vận chuyển + phí lắp đặt
    return gia_goc + phi_van_chuyen + phi_lap_dat


def tinh_khau_hao_nam(gia_goc_ban_dau, so_nam_khau_hao):
    # Mức trích khấu hao năm = Nguyên giá / số năm khấu hao
    return gia_goc_ban_dau / so_nam_khau_hao


def tinh_khau_hao_thang(khau_hao_nam):
    # Mức trích khấu hao tháng = Mức trích khấu hao năm / 12
    return khau_hao_nam / 12


def tinh_khau_hao(gia_goc, so_nam_khau_hao, phi_van_chuyen, phi_lap_dat):
    # Trả về danh sách số tiền khấu hao của từng năm
    gia_goc_ban_dau = tinh_nguyen_gia(gia_goc, phi_van_chuyen, phi_lap_dat)
    ty_le_khau_hao_hang_nam = tinh_khau_hao_nam(gia_goc_ban_dau, so_nam_khau_hao)
    tong_khau_hao_tich_luy = 0
    lich_khau_hao = []
    for nam in range(1, so_nam_khau_hao + 1):
        so_tien_khau_hao = ty_le_khau_hao_hang_nam
        if nam == so_nam_khau_hao:
            # Năm cuối: Nguyên giá - khấu hao luỹ kế
            so_tien_khau_hao = gia_goc_ban_dau - tong_khau_hao_tich_luy
        tong_khau_hao_tich_luy += so_tien_khau_hao
        lich_khau_hao.append(so_tien_khau_hao)

    return lich_khau_hao


def tinh_gia_tri_con_lai(gia_goc, so_nam_khau_hao, phi_van_chuyen, phi_lap_dat):
    # Trả về danh sách giá trị còn lại sau khấu hao của từng năm
    gia_goc_ban_dau = tinh_nguyen_gia(gia_goc, phi_van_chuyen, phi_lap_dat)
    lich_khau_hao = tinh_khau_hao(gia_goc, so_nam_khau_hao, phi_van_chuyen, phi_lap_dat)
    tong_khau_hao_tich_luy = 0
    lich_con_lai = []
    for so_tien_khau_hao in lich_khau_hao:
        tong_khau_hao_tich_luy += so_tien_khau_hao
        lich_con_lai.append(gia_goc_ban_dau - tong_khau_hao_tich_luy)
    return lich_con_lai


if __name__ == "__main__":
    gia_goc = 10000
    so_nam_khau_hao = 5
    phi_van_chuyen = 500
    phi_lap_dat = 200

    lich_khau_hao = tinh_khau_hao(gia_goc, so_nam_khau_hao, phi_van_chuyen, phi_lap_dat)

    print("Lịch khấu hao hàng năm:")
    for nam, so_tien_khau_hao in enumerate(lich_khau_hao, 1):
        print(f"Năm {nam}: {so_tien_khau_hao:.2f} đồng")
