def tinh_khau_hao(gia_mua, phi_vanchuyen, chi_phi_lapdat, so_nam):
    # Nguyên giá TSCĐ = giá mua + phí vận chuyển + phí lắp đặt
    nguyen_gia = gia_mua + phi_vanchuyen + chi_phi_lapdat
    # Mức trích khấu hao năm = Nguyên giá / số năm sử dụng
    khauhao_nam = nguyen_gia / so_nam
    # Mức trích khấu hao tháng = Mức trích khấu hao năm / 12
    khauhao_thang = khauhao_nam / 12
    return nguyen_gia, khauhao_nam, khauhao_thang


def tinh_chitiet_khau_hao(gia_mua, phi_vanchuyen, chi_phi_lapdat, so_nam):
    nguyen_gia = gia_mua + phi_vanchuyen + chi_phi_lapdat
    khauhao_nam = nguyen_gia / so_nam
    chi_tiet = ""
    khauhao_luyke = 0
    for nam in range(1, so_nam + 1):
        if nam == so_nam:
            # Năm cuối: Nguyên giá - khấu hao luỹ kế
            khauhao_nam = nguyen_gia - khauhao_luyke
        khauhao_luyke = khauhao_luyke + khauhao_nam
        con_lai = nguyen_gia - khauhao_luyke
        con_lai_text = f"{con_lai:,.0f}".replace(",", ".")
        chi_tiet = chi_tiet + f"Năm {nam}, Sau khấu hao còn=>{con_lai_text}\n"
    return chi_tiet
