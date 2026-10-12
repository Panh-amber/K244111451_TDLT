# Exercise 1 - Automatic coffee ordering machine
# Coder: Hoang Phuong Anh - K244111451
#
# Đầu vào : số ly Americano, Cafe Latte, Cappuccino; số tiền khách trả
# Đầu ra  : tổng tiền phải trả, tiền thối (hoặc báo không đủ tiền)
# Dữ liệu : giá mỗi ly là hằng số nguyên, số ly và tổng tiền là biến nguyên
# Theo đề (1.4): 3 món cố định nên KHÔNG dùng vòng lặp

# Hằng số giá mỗi ly (won)
PRICE_AMERICANO = 2500
PRICE_LATTE = 3000
PRICE_CAPPUCCINO = 3000

try:
    # Bước 1: in menu và nhận số ly từng loại
    print("Please tell me the drink you ordered.")
    print("Americano:", PRICE_AMERICANO, "| Cafe latte:", PRICE_LATTE,
          "| Cappuccino:", PRICE_CAPPUCCINO)
    noA = int(input("Number of Americano (cups):"))
    noL = int(input("Number of cafe lattes (cups):"))
    noC = int(input("Number of cappuccinos (cups):"))

    # [Debug] số ly không được âm
    if noA < 0 or noL < 0 or noC < 0:
        print("Number of cups must not be negative.")
    else:
        # Bước 2: tính tổng tiền bằng toán tử +=
        sum = 0
        sum += noA * PRICE_AMERICANO   # sum = sum + noA*2500
        sum += noL * PRICE_LATTE       # sum = sum + noL*3000
        sum += noC * PRICE_CAPPUCCINO  # sum = sum + noC*3000
        print("The total amount is:", sum, " money ")

        # Bước 3: nhận tiền và tính tiền thối
        money = int(input("Enter the amount to be paid >>"))
        if money < sum:
            print("Not enough money.")
        else:
            print("Change is", money - sum, " money ")
except ValueError:
    # [Debug] nhập chữ thay vì số -> trước đây chương trình bị crash
    print("Invalid input, please enter an integer number.")
