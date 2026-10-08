def tinh_khau_hao(gia_goc, so_nam_khau_hao, phi_van_chuyen, phi_lap_dat):
    gia_goc_ban_dau = gia_goc + phi_van_chuyen + phi_lap_dat
    ty_le_khau_hao_hang_nam = gia_goc_ban_dau / so_nam_khau_hao
    tong_khau_hao_tich_luy = 0
    lich_khau_hao = []
    for nam in range(1, so_nam_khau_hao + 1):
        so_tien_khau_hao = ty_le_khau_hao_hang_nam
        if nam == so_nam_khau_hao:
            so_tien_khau_hao = gia_goc_ban_dau - tong_khau_hao_tich_luy
        tong_khau_hao_tich_luy += so_tien_khau_hao
        lich_khau_hao.append(so_tien_khau_hao)

    return lich_khau_hao

# Ví dụ sử dụng:
gia_goc = 10000
so_nam_khau_hao = 5
phi_van_chuyen = 500
phi_lap_dat = 200

lich_khau_hao = tinh_khau_hao(gia_goc, so_nam_khau_hao, phi_van_chuyen, phi_lap_dat)

print("Lịch khấu hao hàng năm:")
for nam, so_tien_khau_hao in enumerate(lich_khau_hao, 1):
    print(f"Năm {nam}: {so_tien_khau_hao:.2f} đồng")