# Exercise 2 - Automatic coffee ordering machine (improve)
# Coder: Hoang Phuong Anh - K244111451
#
# Cải tiến Ex1: menu lưu trong 2 list (tên món, giá) và dùng vòng lặp,
# khách chọn nhiều món, xác nhận đơn hàng, tính tổng tiền và tiền thối.

blist = ['Americano', 'Café Latte', 'Cappuccino', 'Oranges', 'Colacola', 'Grapefruit']
plist = [2500, 3000, 3000, 4000, 1500, 4000]
blistUserChoose = []  # số thứ tự món khách chọn
plistUserChoose = []  # số lượng tương ứng

# Bước 1: in menu (tự thay đổi theo độ dài list)
print("No.  Food Name     Price")
for i in range(len(blist)):
    print(f"{i + 1:<3}  {blist[i]:<12}{plist[i]:>6}")
print("Please tell me the drink you ordered.")

# Bước 2: vòng lặp chọn món
while True:
    noFoodName = 0
    # khách phải chọn từ 1 -> n, nhập sai thì hỏi lại
    while noFoodName <= 0 or noFoodName > len(blist):
        strnoFoodName = input("Please choose the food name(enter number)[{}-{}]:".format(1, len(blist)))
        if strnoFoodName.isdigit():
            noFoodName = int(strnoFoodName)
        else:
            noFoodName = 0
    noQuantity = 0
    while noQuantity <= 0:  # số lượng phải > 0
        strnoQuantity = input("Please enter quantity[>0]:")
        if strnoQuantity.isdigit():
            noQuantity = int(strnoQuantity)
        else:
            noQuantity = 0

    # [Debug] chọn lại món đã có thì cộng dồn số lượng, không tách thành 2 dòng
    if noFoodName in blistUserChoose:
        position = blistUserChoose.index(noFoodName)
        plistUserChoose[position] += noQuantity
    else:
        blistUserChoose.append(noFoodName)
        plistUserChoose.append(noQuantity)

    # [Debug] chấp nhận 'no', 'No', 'NO', ' no ' (trước đây chỉ nhận đúng 'no')
    question = input("Do you want to choose another food?(yes/no):")
    if question.strip().lower() == 'no':
        break

# Bước 3: in đơn hàng xác nhận
print("The list of ordered food/drink:")
sum = 0
# [Debug] dùng f-string căn cột thay cho \t để các cột thẳng hàng
print(f"{'Food Name':<12}{'Price':>8}{'Quantity':>10}{'Money':>10}")
for i in range(len(blistUserChoose)):
    foodName = blist[blistUserChoose[i] - 1]
    quantity = plistUserChoose[i]
    unitPrice = plist[blistUserChoose[i] - 1]
    money = quantity * unitPrice
    sum = sum + money
    print(f"{foodName:<12}{unitPrice:>8}{quantity:>10}{money:>10}")
print("The total amount is:", sum, " money ")

# Bước 4: thanh toán, nhập lại đến khi đủ tiền
while True:
    strmoney = input("Enter the amount to be paid >>")
    # isdigit() đã loại số âm (dấu '-') nên không cần kiểm tra money < 0
    if strmoney.isdigit() == False:
        print(strmoney, " is not valid, it should be a positive integer number")
    else:
        money = int(strmoney)
        if money < sum:
            print("Not enough money, you have to pay ", sum, " money ")
        else:
            print("Paid is successfully!")
            if money > sum:
                print("Change is", money - sum, " money")
            break
print("Thank you so much! see you again!")
