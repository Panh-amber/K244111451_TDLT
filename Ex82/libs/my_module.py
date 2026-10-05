def calc_electricity_bill(group, kwh):
    # group = 1: công tơ thẻ trả trước, group = 0: bán lẻ theo bậc thang
    if group == 1:
        total = kwh * 2271
    else:
        if kwh <= 50:
            total = kwh * 1549
        elif kwh <= 100:
            total = 50 * 1549 + (kwh - 50) * 1600
        elif kwh <= 200:
            total = 50 * 1549 + 50 * 1600 + (kwh - 100) * 1858
        elif kwh <= 300:
            total = 50 * 1549 + 50 * 1600 + 100 * 1858 + (kwh - 200) * 2340
        elif kwh <= 400:
            total = 50 * 1549 + 50 * 1600 + 100 * 1858 + 100 * 2340 + (kwh - 300) * 2615
        else:
            total = 50 * 1549 + 50 * 1600 + 100 * 1858 + 100 * 2340 + 100 * 2615 + (kwh - 400) * 2701

    return total